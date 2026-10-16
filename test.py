form simpleInt import simpleInt

def test_normal():
    assert simpleInt(1000, 5, 2) == 100.0
def test_zero_rate():
    assert simpleInt(1000, 0, 2) == 0.0
def test_zero_time():
    assert simpleInt(2000, 10, 3) == 600.0
def test_zero_decimal():
    assert simpleInt(1500, 7, 4) == 420.0
