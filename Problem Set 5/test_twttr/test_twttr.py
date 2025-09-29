from twttr import shorten


def test_upper():
    assert shorten("I'M LEARNING PYTHON") == "'M LRNNG PYTHN"
    assert shorten("MY NAME IS MOHAMED ABDALLAHI") == "MY NM S MHMD BDLLH"


def test_lower():
    assert shorten("attack on titans is the goat") == "ttck n ttns s th gt"
    assert shorten("cr7 is best player of all times") == "cr7 s bst plyr f ll tms"

def test_punctuation():
    assert shorten("!@#$%^&*&^%^^%^&") == "!@#$%^&*&^%^^%^&"
    assert shorten("**(  ^&^ *^ ^&*^ ^* (7&&#%@%@))") == "**(  ^&^ *^ ^&*^ ^* (7&&#%@%@))"
