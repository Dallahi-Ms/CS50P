from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(9)
    assert jar.capacity == 9

def test_test():
    with pytest.raises(ValueError):
        jar = Jar(-4)
    with pytest.raises(ValueError):
        jar = Jar(-99999999)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar = Jar()
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():

    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar = Jar(9)
        jar.deposit(-3)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(7)
        jar.withdraw(9)


