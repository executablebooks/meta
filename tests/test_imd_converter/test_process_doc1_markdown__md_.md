---
chunk_defaults:
  note:
    color: blue
---

Heading {#id1}
=======

Sub-Heading {#id2}
-----------

This is some *text*

A reference to a header \@ref(id1)

A reference to two headings \@cref(id1,id2)

Some inline math: $x = y + z$

Some display math:

$$
\begin{equation} 
  f\left(k\right) = \binom{n}{k} p^k\left(1-p\right)^{n-k}
\end{equation}
$$

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
::: {.outputs}
a = 3
:::
:::

``` {.julia}
using Calculus
derivative(x -> sin(x), 1.0)
```
