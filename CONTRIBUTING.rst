Development
===========

Environment
-----------

Development is currently done using Python 3.11. We recommend using a virtual
environment such as ``venv``:

.. code:: shell

    python3.11 -m venv venv
    source venv/bin/activate

In your virtual environment, please install all packages for
development by running:

.. code:: shell

   pip install .[dev]

If using ZSH, you need to wrap the last term in quotes, `'.[dev]'`.

Installation
------------

To install in editable mode for development, execute:

.. code:: shell

   pip install -e .[dev]

Testing
-------

To run the tests and view coverage, execute:

.. code:: shell

   python -m pytest --cov=kalendar

Directly running pytest may
[produce errors](https://stackoverflow.com/questions/40718770/pytest-running-with-another-version-of-python).
by testing using a Python version or environment different from
the local development environment, hence we recommend running
as above.

Documentation
-------------

Docstrings
^^^^^^^^^^

All public modules, classes and methods should be documented with
`numpy-style <https://numpydoc.readthedocs.io/en/latest/format.html>`__
docstrings.

API documentation structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The API documentation structure is defined in ``api.rst``. The structure
pulls from the docstrings for the modules, classes, and methods using
Sphinx autodocumentation. ReST documentation is used to create navigable
structure.

Build and view
^^^^^^^^^^^^^^

To build the documentation and test your implementation, use the following command:

.. code:: shell

   sphinx-build -b html docs docs/_build

To view the docs, open up ``docs/_build/index.html`` in your
browser.

pre-commit
----------

All code is formatted according to
`black <https://github.com/psf/black>`__ and
`flake8 <https://flake8.pycqa.org/en/latest/>`__ guidelines. The repo is
set-up to use `pre-commit <https://github.com/pre-commit/pre-commit>`__.
So please run ``pre-commit install`` the first time you are editing.
Thereafter all commits will be checked against black and flake8
guidelines

To check if your changes pass pre-commit without committing, run:

.. code:: shell

   pre-commit run --all-files

Packages
--------

The core package does not currently require any additional imports,
and care should be taken before adding any. If necessary, they
should be placed in an ``install_requires`` section of ``setup.cfg``.
Additional development dependencies for testing, documentation, or
development should be specified in the relevant subsection of
``option.extra_requires``.

Package Release
---------------

Features are developed on our ``develop`` branch, with changes tracked
in the “Unreleased” section at the top of ``CHANGELOG.md``. Upon
release, the ``develop`` branch is merged to ``main`` and the release is
tagged according to `semantic
versioning <https://semver.org/spec/v2.0.0.html>`__.

Versioning is handled by
`setuptools_scm <https://github.com/pypa/setuptools_scm>`__, and the
configuration for this can be found in ``pyproject.toml``

The ``kalendar`` package is built and published to
`PyPI <https://pypi.org/project/aa-toolbox/>`__ whenever a new tag is
pushed.
