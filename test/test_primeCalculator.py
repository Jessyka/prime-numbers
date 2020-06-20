from src.prime_calculator import PrimeCalculator

def test_deve_retornar_False_quando_1():
    primeCalculator = PrimeCalculator()
    assert False == primeCalculator.calculate(1)