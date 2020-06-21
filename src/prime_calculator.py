
class PrimeCalculator():
    def calculate(self, number):
        if number == 1:
            return False
        else:
            for index in range(2, number - 1):
                if self.is_divisible(number, index):
                    return False
        return True

    def is_divisible(self, number, divisor):
        return number % divisor == 0