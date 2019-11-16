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
a = 1
print(f"a = {a}")
```

::: {.outputs}
a = 1
:::
:::

::: {.code-cell}
``` {.python}
a += 1
print(f"a = {a}")
```
:::

::: {.code-cell}
:::

::: {.code-cell}
::: {.outputs}
a = 3
:::
:::

``` {.julia}
using Calculus
derivative(x -> sin(x), 1.0)
```
