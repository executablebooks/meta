---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: '.py'
  mimetype: 'text/x-python'
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: '3.6.7'
widgets:
  application/vnd.jupyter.widget-state+json:
    state: {}
    version_major: 2
    version_minor: 0
---

::: {.nb-cell .markdown cell-number="1"}
``` {.metadata}
{}
```

IMarkdown Test Input
====================

This is some markdown, with **bold** and *italic* text.
:::

::: {.nb-cell .markdown cell-number="2"}
``` {.metadata}
imd:
  fillcolor: blue
  type: note
```

This is a note.
:::

::: {.nb-cell .markdown cell-number="3"}
``` {.metadata}
{}
```

This is markdown after a note
:::

::: {.nb-cell .code cell-number="4" kernel="python3" language="python"}
``` {.metadata}
{}
```

``` {.python .code-cell}
a = 1
print("I've just been run :)")
a
```
:::

::: {.nb-cell .markdown cell-number="5"}
``` {.metadata}
{}
```

The next code cell has metadata, with a label referencing @tbl:pandas.
:::

::: {.nb-cell .code cell-number="6" kernel="python3" language="python"}
``` {.metadata}
imd:
  caption: This is a pandas DataFrame.
  label: tbl:pandas
  type: table
```

``` {.python .code-cell}
from pandas import DataFrame
DataFrame([1, 2])
```
:::

::: {.nb-cell .markdown cell-number="7"}
``` {.metadata}
{}
```

Below is a raw cell.
:::

::: {.nb-cell .raw cell-number="8"}
``` {.metadata}
raw_mimetype: text/latex
```

``` {.raw-cell}
I'm a \textbf{LaTeX} cell.
```
:::

::: {.nb-cell .markdown cell-number="9"}
``` {.metadata}
{}
```

Final markdown cell
:::
