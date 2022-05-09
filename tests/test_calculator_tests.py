from implementation.calculator import Calculator

calculator = Calculator()

def test_addition():
    sum = calculator.addition(1,2,3,4,5)
    assert sum == 15

def test_subtraction():
    result = calculator.subtraction(1,2,3,4,5)
    assert result == -15