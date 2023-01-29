"""Dekad extension for ``datetime.date``."""

from __future__ import annotations

import datetime
from typing import Union

# define Dekad class based off of this article
# https://www.aaronoellis.com/articles/subclassing-datetime-date-in-python-3


class Dekad(datetime.date):
    """Dekad extension for ``datetime.date``.

    Extension of the ``datetime.date`` base class for dekads.
    Uses standard yearly definition of dekad where each month
    is composed of 3 dekads, the first 2 comprising the first 1-10,
    and 11-20 days respectively, and the third dekad comprising
    all remaining days of the month. Under the hood, each ``Dekad``
    is stored as the first day of the dekad, so the 1st dekad of a
    month is the 1st, the 2nd is on the 11th, and the 3rd is on the
    21st. Extension of ``datetime.date``
    allows for comparison of dekads and conversion between
    classes and use of existing constructors, methods, and properties,
    with some additions detailed below. For the purposes of the class
    structure, the yearly definition is relied on, but the monthly
    dekad (1st to 3rd) can be accessed using ``dekad_monthly``.

    Base constructor takes year and dekad. Can
    also be constructed directly from ``datetime.date``
    or ``datetime.datetime`` objects and use any
    ``datetime.date`` constructors:

    ``fromdate()``
    ``fromdatetime()``
    ``fromisoformat()``
    ``fromisocalendar()``
    ``fromtimestamp()``
    ``fromordinal()``

    Method to return ``datetime.date`` object
    added, ``todate()``. Other methods remain
    available. Read-only properties ``dekad`` and
    ``dekad_monthly`` added
    alongside year, month, and day.

    Parameters
    ----------
    year : int
        Year.
    dekad : int
        Dekad, from 1 to 36.

    Examples
    --------
    >>> d = Dekad(2022, 01)
    >>> d
    Dekad(2022, 1)
    >>> d.todate()
    datetime.date(2022, 1, 1)
    >>> d - 1
    Dekad(2021, 36)
    >>> d.dekad
    1
    """

    def __new__(cls, year: int, dekad: int):
        """Initialize new ``Dekad``."""
        if dekad < 1 or dekad > 36:
            raise ValueError("Dekad must be between 1 and 36.")
        month = ((dekad - 1) // 3) + 1
        day = 10 * ((dekad - 1) % 3) + 1  # first day of dekad
        return super().__new__(cls, year, month, day)  # noqa: FKA01

    def __repr__(self):
        """Represent ``Dekad``."""
        return f"{self.__class__.__name__}({self.year}, {self.dekad})"

    def __reduce__(self):
        """Reduce."""
        return (self.__class__, (self.year, self.dekad))

    def __str__(self):
        """Print representation."""
        return f"{self.year} D{self.dekad}"

    def __add__(  # type: ignore[override]
        self, other: Union[int, datetime.timedelta]
    ) -> Union[Dekad, datetime.timedelta]:
        """Addition magic method for dekads.

        For integers, adds that to the dekads and returns a new
        ``Dekad`` object. Otherwise, follows the behavior of
        ``datetime.date``.

        Examples
        --------
        >>> d = Dekad(2021, 36)
        >>> d + 1
        Dekad(2022, 1)

        Returns
        -------
        Union[Dekad, datetime.timedelta]
            Returns ``Dekad`` if adding integer, or
            ``datetime.timedelta`` otherwise.
        """
        if isinstance(other, int):
            new_year = self.year + (self.dekad + other) // 36
            new_dekad = self._dekad_adjuster(self.dekad, other)
            return Dekad(year=new_year, dekad=new_dekad)
        else:
            return self.todate() + other

    def __sub__(  # type: ignore[override]
        self, other: Union[int, Dekad, datetime.timedelta]
    ) -> Union[Dekad, int, datetime.timedelta]:
        """Subtraction magic method for dekads.

        For integers, subtracts that from the dekads.
        Dekads can also be subtracted from each other,
        returning the number of dekads between. Otherwise,
        follows the behavior of ``datetime.date``.

        Examples
        --------
        >>> import datetime
        >>>
        >>> d1 = Dekad(2022, 1)
        >>> d2 = Dekad(2021, 1)
        >>> d1 - 1
        Dekad(2021, 36)
        >>> d1 - d2
        36
        >>> d1 - datetime.date(2021, 12, 30)
        datetime.timedelta(days=2)

        Returns
        -------
        Union[Dekad, int, datetime.timedelta]
            Returns ``Dekad`` if subtracting integer, or
            ``int`` if subtracting another ``Dekad``,
            and ``datetime.timedelta`` otherwise.
        """
        if isinstance(other, int):
            new_dekad = self._dekad_adjuster(self.dekad, -other)
            new_year = self.year - (36 - self.dekad + other) // 36
            return Dekad(year=new_year, dekad=new_dekad)
        if isinstance(other, Dekad):
            return self.dekad - other.dekad + 36 * (self.year - other.year)
        else:
            return self.todate() - other

    @property
    def dekad(self):
        """Dekad of the year, 1 to 36."""
        return self._get_dekad(month=self.month, day=self.day)

    @property
    def dekad_monthly(self):
        """Dekad of the month, 1 to 3."""
        return 1 + (self.day - 1) // 10

    def todate(self):
        """Convert to datetime.date object for the year, month, and day."""
        return datetime.date(year=self.year, month=self.month, day=self.day)

    @classmethod
    def fromdate(cls, d: datetime.date) -> Dekad:
        """Construct a dekad from a datetime.date object."""
        dekad = cls._get_dekad(month=d.month, day=d.day)
        return cls(year=d.year, dekad=dekad)

    @classmethod
    def fromdatetime(cls, dt: datetime.datetime) -> Dekad:
        """Construct a dekad from a datetime.date object."""
        dekad = cls._get_dekad(month=dt.month, day=dt.day)
        return cls(year=dt.year, dekad=dekad)

    @classmethod
    def fromisoformat(cls, time_string: str) -> Dekad:
        """Construct a dekad from a string in one of the ISO 8601 formats."""
        return cls.fromdate(datetime.date.fromisoformat(time_string))

    @classmethod
    def fromisocalendar(cls, year: int, week: int, day: int) -> Dekad:
        """Construct a dekad from the ISO year, week number and weekday."""
        return cls.fromdate(
            datetime.date.fromisocalendar(year=year, week=week, day=day)
        )

    @classmethod
    def fromtimestamp(cls, timestamp: float) -> Dekad:
        """Construct a dekad from a POSIX timestamp (like time.time())."""
        return cls.fromdate(datetime.date.fromtimestamp(timestamp))

    @classmethod
    def fromordinal(cls, n: int) -> Dekad:
        """Construct a dekad from a proleptic Gregorian ordinal.

        January 1 of the year 1 is day 1. Only the year, month and day
        are non-zero in the result.
        """
        return cls.fromdate(datetime.date.fromordinal(n))

    @staticmethod
    def _dekad_adjuster(d1: int, d2: int) -> int:
        """Add or subtract d2 from d1 and keep within dekadal ranges."""
        return (d1 + (d2 % 36) + 35) % 36 + 1

    @staticmethod
    def _get_dekad(month: int, day: int) -> int:
        """Get dekad from day and month."""
        return min((day - 1) // 10, 2) + ((month - 1) * 3) + 1
