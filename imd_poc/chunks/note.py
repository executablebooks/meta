from typing import List, Union

import panflute as pf

from .base import BaseChunk


class NoteChunk(BaseChunk):
    """Create a note box."""

    @classmethod
    def declare_options(self) -> dict:
        """Return a JSON schema of chunk options."""
        return {
            "color": {"type": "string", "description": "The color to fill the box."}
        }

    @classmethod
    def declare_formats(self) -> List[str]:
        """Return a list of supported output types."""
        return ["markdown", "html", "latex", "rst"]

    def process_chunk(self, *, text: str, options: dict) -> Union[pf.Block, None]:
        """Process the chunk, and return a pandoc block level element."""
        # TODO merge doc and chunk metadata
        color = ""
        if "color" in options:
            color = options["color"]
        elif "color" in self.doc_metadata.get("chunk_defaults", {}).get("note", {}):
            color = self.doc_metadata["chunk_defaults"]["note"]["color"]
        if self.output_fmt == "latex":
            if color:
                return pf.RawBlock(
                    f"\\begin{{note}}[color={color}]\n{text}\\end{{note}}", format="tex"
                )
            else:
                return pf.RawBlock(
                    f"\\begin{{note}}\n{text}\\end{{note}}", format="tex"
                )
        return pf.Div(
            *pf.convert_text(text), classes=["note"], attributes={"color": color}
        )
