---
chunk_defaults:
  note:
      color: blue
---

# Heading  {#id1}

## Sub-Heading {#id2}

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

```{note}
This is a note.
```

This is some more text.

```{python}
import os
a = 1
b = "I'm a replacement"
c = 1.0
print(f"a = {a}")
```

{{python:b}}

```{python eval=False}
a += 1
print(f"a = {a}")
```

```{python include=False}
a += 1
print(f"a = {a}")
```

```{python echo=False}
a += 1
print(f"a = {a}")
```

{{python:a}}

```{julia, eval=False}
using Calculus
derivative(x -> sin(x), 1.0)
```