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

``` {.python}
a = 1
print("I've just been run :)")
a
```

``` {.yaml .outputs}
- {name: stdout, output_type: stream, text: 'I''ve just been run :)

    '}
- data: {text/plain: '1'}
  execution_count: 1
  metadata: {}
  output_type: execute_result
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

``` {.python}
from pandas import DataFrame
DataFrame([1, 2])
```

``` {.yaml .outputs}
- data: {text/html: "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type\
      \ {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n\
      \        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align:\
      \ right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n\
      \    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n\
      \    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n\
      \    </tr>\n    <tr>\n      <th>1</th>\n      <td>2</td>\n    </tr>\n  </tbody>\n\
      </table>\n</div>", text/plain: '   0

      0  1

      1  2'}
  execution_count: 2
  metadata: {}
  output_type: execute_result
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

``` {.raw}
I'm a \textbf{LaTeX} cell.
```
:::

::: {.nb-cell .markdown cell-number="9"}
``` {.metadata}
{}
```

Final markdown cell
:::
