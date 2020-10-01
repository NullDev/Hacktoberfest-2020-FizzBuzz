def fizzBuzz(n: int) -> list:
    return(['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, n+1)])

if __name__ == '__main__':
    print(fizzBuzz(100))
