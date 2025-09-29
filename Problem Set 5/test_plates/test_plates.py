from plates import is_valid

def test_length():
    assert is_valid(" ") == False
    assert is_valid("D") == False
    assert is_valid("DDD") == True
    assert is_valid("DA44444") == False

def test_beginning():
    assert is_valid("A73") == False
    assert is_valid("AB12") == True
    assert is_valid("12A") == False



def test_number():
    assert is_valid("22AA") == False
    assert is_valid("AA2A22") == False
    assert is_valid("AAA222") == True

def test_punctuation_space():
    assert is_valid("AA!'22") == False
    assert is_valid("CS 50") == False
    assert is_valid("   Har  vard") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("AA20") == True
