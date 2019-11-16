from abc import ABC, abstractmethod
import copy
from typing import List, Union

import panflute as pf


class BaseReference(ABC):

    @classmethod
    @abstractmethod
    def declare_formats(self) -> Union[None, List[str]]:
        """Return a list of supported output types.
        
        None indicates that it supports all outputs
        """
        return []

    def __init__(self, *, output_fmt: str, doc_metadata: dict):
        """Initiate an instance."""
        if output_fmt not in self.declare_formats():
            raise TypeError(
                f"{self.__class__.__name__} is not compatible with '{output_fmt}' outputs"
            )
        self.output_fmt = output_fmt
        self.doc_metadata = copy.deepcopy(doc_metadata)

    @abstractmethod
    def process_reference(self, text: str) -> Union[pf.Inline, None]:
        """Process the reference, and return a pandoc inline element."""
        return None


class Ref(BaseReference):
    def declare_formats(self) -> Union[None, List[str]]:
        """Return a list of supported output types."""
        return ["latex", "html", "markdown", "rst"]
    def process_reference(self, text: str, reference_dict: dict) -> Union[pf.Inline, None]:
        """Process the reference, and return a pandoc inline element."""
        assert "," not in text, "multiple references not allowed"
        if self.output_fmt == "markdown":
            return pf.RawInline(f"\\@ref({text})", format="markdown")
        if self.output_fmt == "rst":
            return pf.RawInline(f":ref:`{text}`", format="rst")
        if self.output_fmt in ["latex", "tex"]:
            return pf.RawInline(f"\\ref{{{text}}}", format="tex")
        if self.output_fmt == "html":
            # TODO
            return pf.RawInline(f'<a href="#{text}">{text}</a>', format="html")

class Cref(BaseReference):
    def declare_formats(self) -> Union[None, List[str]]:
        """Return a list of supported output types."""
        return ["latex", "html", "markdown", "rst"]
    def process_reference(self, text: str, reference_dict: dict) -> Union[pf.Inline, None]:
        """Process the reference, and return a pandoc inline element."""
        if self.output_fmt == "markdown":
            return pf.RawInline(f"\\@cref({text})", format="markdown")
        if self.output_fmt == "rst":
            return pf.RawInline(f":numref:`{text}`", format="rst")
        if self.output_fmt == "latex":
            return pf.RawInline(f"\\cref{{{text}}}", format="tex")
        if self.output_fmt == "html":
            # TODO
            return pf.RawInline(f'<a href="#{text}">{text}</a>', format="html")

class CrefUpper(BaseReference):
    def declare_formats(self) -> Union[None, List[str]]:
        """Return a list of supported output types."""
        return ["latex", "html", "markdown", "rst"]
    def process_reference(self, text: str, reference_dict: dict) -> Union[pf.Inline, None]:
        """Process the reference, and return a pandoc inline element."""
        if self.output_fmt == "markdown":
            return pf.RawInline(f"\\@Cref({text})", format="markdown")
        if self.output_fmt == "rst":
            return pf.RawInline(f":ref:`{text}`", format="rst")
        if self.output_fmt == "latex":
            return pf.RawInline(f"\\Cref{{{text}}}", format="tex")
        if self.output_fmt == "html":
            # TODO
            return pf.RawInline(f'<a href="#{text}">{text}</a>', format="html")