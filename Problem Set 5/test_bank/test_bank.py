from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, Obama") == 0
    assert value("hello, World!") == 0
    assert value("Hello") == 0

def test_starts_with_h():
    assert value("How are you doing.") == 20
    assert value("How can help your Mbarek") == 20
    assert value("Hi there") == 20
    assert value("Have a    nice day") == 20

def test_else():
    assert value("Will you marry me, honey") == 100
    assert value("Ronaldo proposed") == 100
    assert value("good morning") == 100
