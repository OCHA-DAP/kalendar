# kalendar: ``datetime.date`` extension for climate date measurements

[![license](https://img.shields.io/github/license/OCHA-DAP/kalendar.svg)](https://github.com/OCHA-DAP/kalendar/blob/main/LICENSE)
[![Test Status](https://github.com/OCHA-DAP/kalendar/workflows/tests/badge.svg)](https://github.com/OCHA-DAP/kalendar/actions?query=workflow%3Atests)
[![PyPI Status](https://github.com/OCHA-DAP/kalendar/workflows/PyPI/badge.svg)](https://github.com/OCHA-DAP/kalendar/actions?query=workflow%3APyPI)
[![Documentation Status](https://readthedocs.org/projects/kalendar/badge/?version=latest)](https://kalendar.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://codecov.io/gh/OCHA-DAP/kalendar/branch/main/graph/badge.svg?token=JpWZc5js4y)](https://codecov.io/gh/OCHA-DAP/kalendar)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

In climatology, data is often reported in multi-day formats, such
as dekads (a 10 day definition) or pentads (a 5 day definition).
kalendar is a Python package with ``datetime.date`` extensions
for dekadal and pentadal (coming) calendar definitions that make
it easier to work with such climate data.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```shell
pip install kalendar
```

## Usage

The dekadal and pentadal classes are simple subclasses with convenient
constructors for creating the class from ``datetime`` objects (and
inherited constructors from ``datetime.date``), methods for addition
and subtraction, and converting back to ``datetime.date`` objects.

```python
from kalendar import Dekad
d = Dekad(2022, 1)
d - 1
```

See the [documentation](https://kalendar.readthedocs.io/en/latest/) for
full examples.

## Contributing

For guidance on setting up a development environment, see the
[contributing guidelines](https://github.com/OCHA-DAP/kalendar/blob/main/CONTRIBUTING.rst)

## Links

- [Documentation](https://kalendar.readthedocs.io/en/latest/)
- [Changes](https://github.com/OCHA-DAP/kalendar/blob/main/CHANGELOG.rst)
- [PyPI Releases](https://pypi.org/project/kalendar/)
- [Source Code](https://github.com/OCHA-DAP/kalendar)
- [Issue Tracker](https://github.com/OCHA-DAP/kalendar/issues)
