Welcome to kalendar
===================

Welcome to kalendar's documentation!

In climatology, data is often reported in multi-day formats, such
as dekads (a 10 day definition) or pentads (a 5 day definition).
kalendar is a Python package with ``datetime.date`` extensions
for dekadal and pentadal (coming) calendar definitions that make
it easier to work with such climate data.

The dekadal and pentadal classes are simple subclasses with convenient
constructors for creating the class from ``datetime`` objects (and
inherited constructors from ``datetime.date``), methods for addition
and subtraction, and converting back to ``datetime.date`` objects.

.. code-block:: python

   from kalendar import Dekad
   d = Dekad(2022, 1)
   d - 1

The below API provides more details and examples on the classes' usage.

API Reference
-------------

Details of the classes in the kalendar package.

.. toctree::
   :maxdepth: 1

   api

Miscellaneous
-------------

Development guide, license, and changelog.

.. toctree::
   :maxdepth: 2

   contributing
   license
   changelog
