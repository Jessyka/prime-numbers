from src.prime_calculator import PrimeCalculator

def test_deve_retornar_False_quando_1():
    primeCalculator = PrimeCalculator()
    assert False == primeCalculator.calculate(1)

def test_deve_retornar_True_quando_2():
    primeCalculator = PrimeCalculator()
    assert True == primeCalculator.calculate(2)

def test_deve_retornar_False_quando_4():
    primeCalculator = PrimeCalculator()
    assert False == primeCalculator.calculate(4)