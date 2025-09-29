from working import convert
import pytest

def test_raising():
    with pytest.raises(ValueError):
        convert("7:60 PM to 9:60 AM")
    with pytest.raises(ValueError):
        convert("7:19 to 9:30 AM")
    with pytest.raises(ValueError):
        convert("9 AM - 10:30 PM")
    with pytest.raises(ValueError):
        convert("9:30 PM to 17:30")

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("3:25 PM to 4:25 PM") == "15:25 to 16:25"

def test_midnight():
    assert convert("12:23 AM to 12:00 PM") == "00:23 to 12:00"




