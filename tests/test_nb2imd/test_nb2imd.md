---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.6.7
widgets:
  application/vnd.jupyter.widget-state+json:
    state: {}
    version_major: 2
    version_minor: 0
---

# IMarkdown Test Input

This is some markdown, with **bold** and *italic* text.

```metadata
imd:
  fillcolor: blue
  type: note
```

This is a note.

[]{.new-cell}

This is markdown after a note

```python
a = 1
print("I've just been run :)")
a
```

The next code cell has metadata.

```metadata
imd:
  caption: This is a pandas DataFrame.
  label: tbl:pandas
  type: table
```

```python
from pandas import DataFrame
DataFrame([1, 2])
```

Below is a raw cell.

```metadata
raw_mimetype: text/latex
```

```raw
I'm a \textbf{LaTeX} cell.
```

Final markdown cell
