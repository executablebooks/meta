.. _id1:

Heading
=======

.. _id2:

Sub-Heading
-----------

This is some *text*

A reference to a header :ref:`id1`

A reference to two headings :numref:`id1,id2`

Some inline math: :math:`x = y + z`

Some display math:

.. math::


   \begin{equation} 
     f\left(k\right) = \binom{n}{k} p^k\left(1-p\right)^{n-k}
   \end{equation}

.. note::

   This is a note.

This is some more text.

.. container:: code-cell

   .. code:: python

      a = 1
      print(f"a = {a}")

   .. container:: outputs

      a = 1

.. container:: code-cell

   .. code:: python

      a += 1
      print(f"a = {a}")

.. container:: code-cell

   .. container:: outputs

      a = 3

.. code:: julia

   using Calculus
   derivative(x -> sin(x), 1.0)
