IntCode
=======

- https://esolangs.org/wiki/Intcode
- https://adventofcode.com/2019

In particular I am using day 21's implementation of the IntCode computer.  In
this version of the IntCode computer, the output instruction receives
ASCII integers and prints those characters to the screen.

Here's a sample execution of my FizzBuzz program:

```console
$ python3 ../part1.py IntCode/asottile.txt
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz
> 88414 μs
```

Here's the rough algorithm I used, translated into python

```python
from typing import Tuple


def divmod(n: int, mod: int) -> Tuple[int, int]:
    """implement divison + mod using addition"""
    i = 0
    sub = -1 * mod

    while n >= mod:
        n += sub
        i += 1

    return i, n


def printnum(n: int) -> None:
    # build up a divisor, we'll use this to print one digit at a time
    tens = 10
    while not n < tens:
        tens *= 10
    tens, _ = divmod(tens, 10)

    # print one digit at a time while moving the divisor down
    while tens != 0:
        tmp1, _ = divmod(n, tens)
        _, tmp1 = divmod(tmp1, 10)
        tmp1 += ord('0')
        print(chr(tmp1), end='')

        tens, _ = divmod(tens, 10)


def main() -> int:
    start = 1
    end = 100
    started = 0

    while start <= end:
        if started:
            print(', ', end='')
        started = 1

        _, remainder_3 = divmod(start, 3)
        _, remainder_5 = divmod(start, 5)
        both_non_divisible = remainder_3 * remainder_5

        if remainder_3 == 0:
            print('Fizz', end='')
        if remainder_5 == 0:
            print('Buzz', end='')
        if both_non_divisible:
            printnum(start)

        start += 1

    print('\n', end='')
    return 0


if __name__ == '__main__':
    exit(main())
```
