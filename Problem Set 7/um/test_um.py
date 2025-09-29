from um import count

def test_cases():
    assert count("UM um Um uM") == 4
    assert count("um can i get the certificate Um...") == 2
    assert count("UM UM") == 2

def test_words():
    assert count("umbrella ") == 0
    assert count("Album") == 0
    assert count("Hey, hello beautiful um.. Can I get your number") == 1

