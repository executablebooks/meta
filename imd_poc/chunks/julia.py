from typing import List, Union

import panflute as pf

from .base import BaseChunk, ChunkResult


class JuliaChunk(BaseChunk):
    """Run and format julia code cells."""

    @classmethod
    def declare_options(self) -> dict:
        """Return a JSON schema of chunk options."""
        return {}

    @classmethod
    def declare_formats(self) -> List[str]:
        """Return a list of supported output formats."""
        return ["markdown", "html", "latex", "rst"]

    def process_chunk(self, *, text: str, options: dict) -> ChunkResult:
        """Process the chunk, and return a pandoc block level element."""
        return ChunkResult(pf.CodeBlock(text, classes=["julia"]))
