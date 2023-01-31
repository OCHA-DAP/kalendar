"""kalendar module of datetime.date extensions."""

from ._version import __version__
from .dekad import Dekad
from .pentad import Pentad

__all__ = ["Dekad", "Pentad", "__version__"]
