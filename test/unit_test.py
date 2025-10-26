from src.mathematical_operations import add, subtract 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0 
    assert add(3, 4) == 7 
    assert add(7, 8) == 15

def test_subtract():
    assert subtract(-1, -2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(1, -1) == 2
    assert subtract(1, 1) == 0