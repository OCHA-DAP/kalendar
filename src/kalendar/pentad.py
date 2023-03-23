"""Pentad extension for ``datetime.date``."""

from __future__ import annotations

import calendar
import datetime
from typing import Union

# define Pentad class based off of this article
# https://www.aaronoellis.com/articles/subclassing-datetime-date-in-python-3


class Pentad(datetime.date):
    """Pentad extension for ``datetime.date``.

    Extension of the ``datetime.date`` base class for pentads.
    Uses standard yearly definition of pentads where the 365 day
    calendar year is divided into 73 pentads of 5 days each.
    Under the hood, each ``Pentad``
    is stored as the first day of the pentad, the 1st pentad of the year
    is on January 1st, the 2nd on January 6th, and so on. Leap years have
    366 days, and pentad 12 is extended comprise 6 days that
    includes February 29th. Extension of ``datetime.date``
    allows for comparison of pentads and conversion between
    classes and use of existing constructors, methods, and properties,
    with some additions detailed below.

    Base constructor takes year and pentad. Can
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
    available. Read-only property ``pentad``
    added alongside year, month, and day.

    Parameters
    ----------
    year : int
        Year.
    pentad : int
        Pentad, from 1 to 73.

    Examples
    --------
    >>> p = Pentad(2022, 1)
    >>> p
    Pentad(2022, 1)
    >>> p.todate()
    datetime.date(2022, 1, 1)
    >>> p - 1
    Pentad(2021, 73)
    >>> p.pentad
    1
    """

    def __new__(cls, year: int, pentad: int):
        """Initialize new ``Pentad``."""
        if pentad < 1 or pentad > 73:
            raise ValueError("Pentad must be between 1 and 73.")

        # get pentad month and day from non-leap year
        dt = datetime.date(year=2010, month=1, day=1) + datetime.timedelta(
            (pentad - 1) * 5
        )

        return super().__new__(cls, year, dt.month, dt.day)  # noqa: FKA01

    def __repr__(self):
        """Represent ``Pentad``."""
        return f"{self.__class__.__name__}({self.year}, {self.pentad})"

    def __reduce__(self):
        """Reduce."""
        return (self.__class__, (self.year, self.pentad))

    def __str__(self):
        """Print representation."""
        return f"{self.year} P{self.pentad}"

    def __add__(  # type: ignore[override]
        self, other: Union[int, datetime.timedelta]
    ) -> Union[Pentad, datetime.date]:
        """Addition magic method for pentads.

        For integers, adds that to the pentads and returns a new
        ``Pentad`` object. Otherwise, follows the behavior of
        ``datetime.date``.

        Examples
        --------
        >>> p = Pentad(2021, 73)
        >>> p + 1
        Pentad(2022, 1)

        Returns
        -------
        Union[Pentad, datetime.date]
            Returns ``Pentad`` if adding integer, or
            ``datetime.date`` otherwise.
        """
        if isinstance(other, int):
            new_year = self.year + (self.pentad + other - 1) // 73
            new_pentad = self._pentad_adjuster(self.pentad, other)
            return Pentad(year=new_year, pentad=new_pentad)  # type: ignore
        try:
            return self.todate() + other
        except TypeError as e:
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'Pentad' and {type(other).__name__}"
            ) from e

    def __sub__(  # type: ignore[override]
        self, other: Union[int, Pentad, datetime.timedelta]
    ) -> Union[Pentad, int, datetime.timedelta]:
        """Subtraction magic method for pentads.

        For integers, subtracts that from the pentads.
        Pentads can also be subtracted from each other,
        returning the number of pentads between. Otherwise,
        follows the behavior of ``datetime.date``.

        Examples
        --------
        >>> import datetime
        >>>
        >>> p1 = Pentad(2022, 1)
        >>> p2 = Pentad(2021, 1)
        >>> p1 - 1
        Pentad(2021, 73)
        >>> p1 - p2
        73
        >>> p1 - datetime.date(2021, 12, 30)
        datetime.timedelta(days=2)

        Returns
        -------
        Union[Pentad, int, datetime.timedelta]
            Returns ``Pentad`` if subtracting integer, or
            ``int`` if subtracting another ``Pentad``,
            and ``datetime.timedelta`` otherwise.
        """
        if isinstance(other, int):
            new_pentad = self._pentad_adjuster(self.pentad, -other)
            new_year = self.year - (73 - self.pentad + other) // 73
            return Pentad(year=new_year, pentad=new_pentad)
        if isinstance(other, Pentad):
            pentad_diff = self.pentad - other.pentad
            year_diff = 73 * (self.year - other.year)
            return pentad_diff + year_diff  # type: ignore
        try:
            return self.todate() - other  # type: ignore
        except TypeError as e:
            raise TypeError(
                f"unsupported operand type(s) for -: "
                f"'Pentad' and {type(other).__name__}"
            ) from e

    @property
    def pentad(self) -> int:
        """Pentad of the year, 1 to 73."""
        return self._get_pentad(dt=self.todate())

    def todate(self) -> datetime.date:
        """Convert to datetime.date object for the year, month, and day."""
        return datetime.date(year=self.year, month=self.month, day=self.day)

    @classmethod
    def fromdate(cls, d: datetime.date) -> Pentad:
        """Construct a pentad from a datetime.date object."""
        pentad = cls._get_pentad(dt=d)
        return cls(year=d.year, pentad=pentad)

    @classmethod
    def fromdatetime(cls, dt: datetime.datetime) -> Pentad:
        """Construct a pentad from a datetime.date object."""
        pentad = cls._get_pentad(dt=dt)
        return cls(year=dt.year, pentad=pentad)

    @classmethod
    def fromisoformat(cls, time_string: str) -> Pentad:
        """Construct a pentad from a string in one of the ISO 8601 formats."""
        return cls.fromdate(datetime.date.fromisoformat(time_string))

    @classmethod
    def fromisocalendar(cls, year: int, week: int, day: int) -> Pentad:
        """Construct a pentad from the ISO year, week number and weekday."""
        return cls.fromdate(
            datetime.date.fromisocalendar(year=year, week=week, day=day)
        )

    @classmethod
    def fromtimestamp(cls, timestamp: float) -> Pentad:
        """Construct a pentad from a POSIX timestamp (like time.time())."""
        return cls.fromdate(datetime.date.fromtimestamp(timestamp))

    @classmethod
    def fromordinal(cls, n: int) -> Pentad:
        """Construct a pentad from a proleptic Gregorian ordinal.

        January 1 of the year 1 is day 1. Only the year, month and day
        are non-zero in the result.
        """
        return cls.fromdate(datetime.date.fromordinal(n))

    @staticmethod
    def _pentad_adjuster(p1: int, p2: int) -> int:
        """Add or subtract p2 from p1 and keep within pentadal ranges."""
        return (p1 + (p2 % 73) + 72) % 73 + 1

    @staticmethod
    def _get_pentad(dt: datetime.date) -> int:
        """Get pentad from datetime."""
        yday = dt.timetuple().tm_yday
        if calendar.isleap(dt.year) and yday >= 60:
            return 1 + (yday - 2) // 5
        else:
            return 1 + (yday - 1) // 5
