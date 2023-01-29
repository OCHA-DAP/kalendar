# kalendar: ``datetime.date`` extension for climate date measurements

In climatology, data is often reported in multi-day formats, such
as dekads (a 10 day definition) or pentads (a 5 day definition).
kalendar is a Python package with ``datetime.date`` extensions
for dekadal and pentadal calendar definitions that make it easier
to work with such climate data.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```shell
pip install kalendar
```

## Usage

The dekadal and pentadal classes are simple subclasses with convenient
constructors for creating the class from ``datetime`` objects (and
inherited constructors from ``datetime.date``), methods for addition
and subtraction, and converting back to ``datetime.date`` objects. See the
documentation for full examples.

```python
from kalendar import Dekad
d = Dekad(2022, 1)
d - 1
```

## Contributing

For guidance on setting up a development environment, see the
[contributing guidelines](https://github.com/OCHA-DAP/kalendar/blob/main/CONTRIBUTING.rst)

## Links

- [Documentation](https://kalendar.readthedocs.io/en/latest/)
- [Changes](https://github.com/OCHA-DAP/kalendar/blob/main/CHANGELOG.rst)
- [PyPI Releases](https://pypi.org/project/kalendar/)
- [Source Code](https://github.com/OCHA-DAP/kalendar)
- [Issue Tracker](https://github.com/OCHA-DAP/kalendar/issues)
