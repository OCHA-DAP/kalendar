"""Test dekad module."""

import pickle
from datetime import date, datetime, timedelta

import pytest

from kalendar import Dekad


@pytest.fixture
def dekad():
    """Dekad fixture."""
    return Dekad(year=2022, dekad=1)


def test_addition(dekad):
    """Test addition magic method."""
    assert dekad + 1 == Dekad(2022, 2)
    assert dekad + 38 == Dekad(2023, 3)
    assert dekad + timedelta(days=1) == date(year=2022, month=1, day=2)


def test_subtraction(dekad):
    """Test subtraction magic method."""
    assert dekad - 1 == Dekad(2021, 36)
    assert dekad - 38 == Dekad(2020, 35)
    assert dekad - Dekad(2021, 34) == 3
    assert dekad - date(year=2021, month=12, day=20) == timedelta(days=12)


def test_repr(dekad):
    """Test repr magic method."""
    assert eval(repr(dekad)) == dekad


def test_pickling(dekad):
    """Test that pickling works on the class.

    Magic methods sometimes need to be adjusted for
    subclassing or pickling will generate errors.
    This ensures that it's always possible. Based
    on the article that inspired the class.

    https://www.aaronoellis.com/articles/subclassing-datetime-date-in-python-3
    """
    assert pickle.loads(pickle.dumps(dekad)) == dekad


def test_todate(dekad):
    """Test the todate() method."""
    assert dekad.todate() == date(year=2022, month=1, day=1)
    d = Dekad(year=2008, dekad=32)
    assert d.todate() == date(year=2008, month=11, day=11)


def test_constructors(dekad):
    """Test constructor methods."""
    assert Dekad.fromisocalendar(year=2022, week=1, day=7) == dekad
    assert Dekad.fromisoformat("2022-01-10") == dekad
    assert Dekad.fromordinal(738161) == dekad
    assert Dekad.fromdate(date(year=2022, month=1, day=5))
    # datetime
    dt = datetime(year=2022, month=1, day=8)
    assert Dekad.fromtimestamp(dt.timestamp()) == dekad
    assert Dekad.fromdatetime(dt) == dekad


def test_constructors_error():
    """Test constructor error."""
    with pytest.raises(ValueError):
        Dekad(2022, -1)
    with pytest.raises(ValueError):
        Dekad(2011, 37)


def test_printing(dekad, capsys):
    """Test printing."""
    print(dekad)  # noqa: T001
    out, _ = capsys.readouterr()
    assert out == "2022 D1\n"


def test_dekad_month(dekad):
    """Test monthly dekad."""
    assert dekad.dekad_monthly == 1
    assert (dekad + 2).dekad_monthly == 3
