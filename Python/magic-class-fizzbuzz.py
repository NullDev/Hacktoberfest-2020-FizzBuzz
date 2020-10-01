# Description: An implementation using a class and magic methods
# @Author: Oxel40


class FizzBuzz:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        if self.n % 3 == 0 and self.n % 5 == 0:
            return "FizzBuzz"
        if self.n % 3 == 0:
            return "Fizz"
        if self.n % 5 == 0:
            return "Buzz"
        return str(self.n)


if __name__ == '__main__':
    print(*[FizzBuzz(x) for x in range(1, 101)], sep='\n')
