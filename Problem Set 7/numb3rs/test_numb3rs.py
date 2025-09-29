from numb3rs import validate

def test_words():
    assert validate("cat") == False
    assert validate("CS50.P") == False
    assert validate("") == False
    assert validate("....") == False

def test_big():
    assert validate("0.0.0.1") == True
    assert validate("444.234.32.443") == False
    assert validate("255.255.255.255") == True
    assert validate("256.257.258.259") == False
    assert validate("457.2332.3423.999.") == False

def test_spaces():
    assert validate(" . . . ") == False
    assert validate("2 . 22 . . 2") == False
    assert validate("  ") == False
    assert validate("23.255 .200.99") == False

def test_short():
    assert validate("1.2") == False
    assert validate("1.2.3") == False
    assert validate("1.") == False

def test_noP():
    assert validate("1 2 3 4") == False
    assert validate("1.2.3 4") == False
    assert validate("1.2 3.4") == False

def test_math():
    assert validate("1+2.3.4.122") == False
    assert validate("-255.255.255.255") == False
    assert validate("2.-3.260-20.4") == False
