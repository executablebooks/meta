from contextlib import contextmanager

from nbconvert.preprocessors.execute import (
    ExecutePreprocessor,
    CellExecutionComplete,
    Empty,
)
from panflute import Doc, Div, CodeBlock
from panflute.tools import meta2builtin
import yaml

from .definitions import NB_CELL_CLASS, CELL_NUMBER_ATTR
from imd_poc.nb2imd import mapping_to_dict


class SourceExecuter(ExecutePreprocessor):
    """This is a first stab at an executor that runs directly on source code."""

    @contextmanager
    def setup_preprocessor(self):
        self._display_id_map = {}
        self.widget_state = {}
        self.widget_buffers = {}
        self.km, self.kc = self.start_new_kernel(cwd=None)
        try:
            yield self.km, self.kc
        finally:
            self.kc.stop_channels()
            self.km.shutdown_kernel(now=self.shutdown_kernel == "immediate")
            delattr(self, "km")
            delattr(self, "kc")

    def run_cell(self, source, cell_index=None):
        parent_msg_id = self.kc.execute(source)
        self.log.debug("Executing cell:\n%s", source)
        exec_reply = self._wait_for_reply(parent_msg_id)
        outputs = []
        self.clear_before_next_output = False

        while True:
            try:
                msg = self.kc.iopub_channel.get_msg(timeout=self.iopub_timeout)
            except Empty:
                self.log.warning("Timeout waiting for IOPub output")
                if self.raise_on_iopub_timeout:
                    raise RuntimeError("Timeout waiting for IOPub output")
                else:
                    break
            if msg["parent_header"].get("msg_id") != parent_msg_id:
                # not an output from our execution
                continue
            # Will raise CellExecutionComplete when completed
            try:
                self.process_message(msg, outputs, cell_index)
            except CellExecutionComplete:
                break

        return exec_reply, outputs

    def process_message(self, msg, outputs, cell_index):
        msg_type = msg["msg_type"]
        self.log.debug("msg_type: %s", msg_type)
        content = msg["content"]
        self.log.debug("content: %s", content)
        display_id = content.get("transient", {}).get("display_id", None)
        if display_id and msg_type in {
            "execute_result",
            "display_data",
            "update_display_data",
        }:
            self._update_display_id(display_id, msg)
        if msg_type == "status":
            if content["execution_state"] == "idle":
                raise CellExecutionComplete()
        elif msg_type.startswith("comm"):
            self.handle_comm_msg(outputs, msg, cell_index)
        # Check for remaining messages we don't process
        elif msg_type not in ["execute_input", "update_display_data"]:
            # Assign output as our processed "result"
            return self.output(outputs, msg, display_id, cell_index)


def exec_code_cells(doc: Doc):
    """Execute a code cells, in a document that has been created via ```Imd2PandocAST```."""
    doc_metadata = meta2builtin(doc.metadata)
    kernel_name = doc_metadata.get("kernelspec", {}).get("name", "python3")
    executer = SourceExecuter(kernel_name=kernel_name)
    with executer.setup_preprocessor():
        for element in doc.content:
            if isinstance(element, Div) and {NB_CELL_CLASS, "code"}.issubset(
                element.classes
            ) and element.attributes.get("kernel", None) == kernel_name:
                code_block = element.content[1]
                cell_number = int(element.attributes[CELL_NUMBER_ATTR])
                exec_reply, outputs = executer.run_cell(
                    code_block.text, cell_number
                )
                element.content.append(
                    CodeBlock(yaml.safe_dump(mapping_to_dict(outputs)), classes=["yaml", "outputs"])
                )
