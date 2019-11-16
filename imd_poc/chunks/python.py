from contextlib import contextmanager
from typing import List, Union

from nbconvert.preprocessors.execute import (
    ExecutePreprocessor,
    CellExecutionComplete,
    Empty,
)
import panflute as pf
import yaml

from .base import BaseChunk
from imd_poc.utils import mapping_to_dict


class PythonChunk(BaseChunk):
    """Run and format python code cells."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kernels = {}

    @classmethod
    def declare_options(self) -> dict:
        return {
            "eval": {
                "type": "boolean",
                "description": "If False, the code in the code chunk will not be run.",
                "default": False,
            },
            "include": {
                "type": "boolean",
                "description": "If False, the code in the code chunk will be run, but the code and output will not be output in the final document.",
                "default": True,
            },
            "echo": {
                "type": "boolean",
                "description": "If False, the code in the code chunk will not be displayed above it's results.",
                "default": True,
            },
        }

    @classmethod
    def declare_formats(self) -> List[str]:
        """Return a list of supported output types."""
        return ["markdown", "html", "latex"]

    def process_chunk(self, *, text: str, options: dict) -> Union[pf.Block, None]:
        """Process the chunk, and return a pandoc block level element."""
        blocks = [pf.CodeBlock(text, classes=["python"])]
        if options.get("eval", True):
            kernel_name = self.doc_metadata.get("kernelspec", {}).get("name", "python3")
            if kernel_name not in self.kernels:
                executer = SourceExecuter(kernel_name=kernel_name)
                executer.start_kernel()
                self.kernels[kernel_name] = executer
            exec_reply, outputs = self.kernels[kernel_name].run_cell(text)
            doc_output_els = self.create_output_els(outputs, options)
            if not options.get("include", True):
                blocks = []
            elif not options.get("echo", True):
                blocks = [doc_output_els]
            else:
                blocks += [doc_output_els]
        return pf.Div(*blocks, classes=["code-cell"])

    def clean_up(self):
        for kernel in self.kernels.values():
            kernel.stop_kernel()
        self.kernels = {}

    def create_output_els(self, outputs: List[dict], options: dict) -> pf.Block:
        """Create the output document element, from a JSON of outputs."""
        elements = []
        for output in outputs:
            if output.get("output_type", "stdout"):
                elements.append(pf.Para(pf.Str(output["text"])))
        return pf.Div(*elements, classes=["outputs"])
        # return pf.CodeBlock(
        #         yaml.safe_dump(mapping_to_dict(outputs)), classes=["yaml", "outputs"]
        #     )


class SourceExecuter(ExecutePreprocessor):
    """This is a first stab at an executor that runs directly on source code."""

    def start_kernel(self):
        self._display_id_map = {}
        self.widget_state = {}
        self.widget_buffers = {}
        self.km, self.kc = self.start_new_kernel(cwd=None)
        return self.km, self.kc

    def stop_kernel(self):
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
