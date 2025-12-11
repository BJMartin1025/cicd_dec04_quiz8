import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, multiply, divide, power, sqrt, percentage, log, sin, cos, tan

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 4) == 6

def test_sub2():
    assert sub(10, 4) != 5

def test_multiply():
    assert multiply(3, 7) == 21

def test_multiply2():
    assert multiply(3, 7) != 20

def test_divide():
    assert divide(20, 4) == 5

def test_divide2():
    assert divide(20, 0) == "Error: Division by zero"

def test_power():
    assert power(2, 3) == 8

def test_power2():
    assert power(2, 3) != 9

def test_sqrt():
    assert sqrt(16) == 4

def test_sqrt2():
    assert sqrt(-4) == "Error: Square root of negative number"

def test_percentage():
    assert percentage(20, 50) == 10

def test_percentage2():
    assert percentage(20, 50) != 15

def test_log():
    assert log(100, 10) == 2

def test_log2():
    assert log(-10, 10) == "Error: Logarithm of non-positive number"

def test_sin():
    assert round(sin(30), 5) == 0.5

def test_cos():
    assert round(cos(60), 5) == 0.5

def test_tan():
    assert round(tan(45), 5) == 1.0