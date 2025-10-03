from seasons import transfer
import pytest

def test_errors():
    with pytest.raises(SystemExit):
        transfer("Junuary 1, 1999")
