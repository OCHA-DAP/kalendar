"""Test pentad module."""

import pickle
from datetime import date, datetime, timedelta

import pytest

from kalendar import Pentad


@pytest.fixture
def pentad():
    """Pentad fixture."""
    return Pentad(year=2022, pentad=1)


def test_addition(pentad):
    """Test addition magic method."""
    assert pentad + 1 == Pentad(2022, 2)
    assert pentad + 72 == Pentad(2022, 73)
    assert pentad + 75 == Pentad(2023, 3)
    assert pentad + timedelta(days=1) == date(year=2022, month=1, day=2)


def test_subtraction(pentad):
    """Test subtraction magic method."""
    assert pentad - 1 == Pentad(2021, 73)
    assert pentad - 75 == Pentad(2020, 72)
    assert pentad - Pentad(2021, 71) == 3
    assert pentad - date(year=2021, month=12, day=20) == timedelta(days=12)


def test_repr(pentad):
    """Test repr magic method."""
    assert eval(repr(pentad)) == pentad


def test_pickling(pentad):
    """Test that pickling works on the class.

    Magic methods sometimes need to be adjusted for
    subclassing or pickling will generate errors.
    This ensures that it's always possible. Based
    on the article that inspired the class.

    https://www.aaronoellis.com/articles/subclassing-datetime-date-in-python-3
    """
    assert pickle.loads(pickle.dumps(pentad)) == pentad


def test_todate(pentad):
    """Test the todate() method."""
    assert pentad.todate() == date(year=2022, month=1, day=1)
    p = Pentad(year=2008, pentad=32)
    assert p.todate() == date(year=2008, month=6, day=5)


def test_constructors(pentad):
    """Test constructor methods."""
    assert Pentad.fromisocalendar(year=2022, week=1, day=3) == pentad
    assert Pentad.fromisoformat("2022-01-03") == pentad
    assert Pentad.fromordinal(738157) == pentad
    assert Pentad.fromdate(date(year=2022, month=1, day=5))
    # datetime
    dt = datetime(year=2022, month=1, day=1)
    assert Pentad.fromtimestamp(dt.timestamp()) == pentad
    assert Pentad.fromdatetime(dt) == pentad


def test_constructors_error():
    """Test constructor error."""
    with pytest.raises(ValueError):
        Pentad(2022, -1)
    with pytest.raises(ValueError):
        Pentad(2011, 75)


def test_printing(pentad, capsys):
    """Test printing."""
    print(pentad)  # noqa: T001
    out, _ = capsys.readouterr()
    assert out == "2022 P1\n"


def test_leapyears():
    """Test dates during leap years."""
    p = Pentad(2012, 12)
    assert p.todate() == date(year=2012, month=2, day=25)
    assert (p + 1).todate() == date(year=2012, month=3, day=2)
    assert Pentad.fromisoformat("2012-02-29") == p
    assert Pentad.fromisoformat("2012-12-27").pentad == 73
