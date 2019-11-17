from typing import List, Union

import panflute as pf

from .base import BaseChunk, ChunkResult


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

    def process_chunk(self, *, text: str, options: dict) -> ChunkResult:
        """Process the chunk, and return a pandoc block level element."""
        # TODO merge doc and chunk metadata
        color = ""
        if "color" in options:
            color = options["color"]
        elif "color" in self.doc_metadata.get("chunk_defaults", {}).get("note", {}):
            color = self.doc_metadata["chunk_defaults"]["note"]["color"]
        if self.output_fmt == "latex":
            if color:
                return ChunkResult(pf.RawBlock(
                    f"\\begin{{note}}[color={color}]\n{text}\\end{{note}}", format="tex"
                ))
            else:
                return ChunkResult(pf.RawBlock(
                    f"\\begin{{note}}\n{text}\\end{{note}}", format="tex"
                ))
        return ChunkResult(pf.Div(
            *pf.convert_text(text), classes=["note"], attributes={"color": color}
        ))
