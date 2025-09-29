from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(70) == "70%"

def test_convert():
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("1/4") == 25

def test_both():
    assert convert("2/4") == 50 and gauge(50) == "50%"
    assert convert("4/4") == 100 and gauge(100) == "F"

def test_error():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-4/4")
    with pytest.raises(ValueError):
        convert("3/-4")


