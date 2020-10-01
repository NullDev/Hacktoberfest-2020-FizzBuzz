# Description: recursive FizzBuzz
# @Author: Oxel40


def fizzbuzz(n, end):
    if n == end:
        return
    p = False
    if n % 3 == 0:
        print('Fizz', end='')
        p = True
    if n % 5 == 0:
        print('Buzz', end='')
        p = True
    if not p:
        print(n, end='')
    print()
    fizzbuzz(n+1, end)


if __name__ == '__main__':
    fizzbuzz(1, 101)
