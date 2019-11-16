---
chunk_defaults:
  note:
    color: blue
---

Heading
=======

Sub-Heading
-----------

This is some *text*

::: {.note color="blue"}
This is a note.
:::

This is some more text.

::: {.code-cell}
``` {.python}
print("hallo")
```

::: {.outputs}
hallo
:::
:::

::: {.code-cell}
``` {.python}
print("hallo2")
```
:::

::: {.code-cell}
:::

::: {.code-cell}
::: {.outputs}
hallo4
:::
:::

``` {.julia}
using Calculus
derivative(x -> sin(x), 1.0)
```
