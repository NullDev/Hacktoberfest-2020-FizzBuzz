#!/usr/bin/env python3
# author: @tddschn
# checking if a num is the multiples of 3 or 5 or 15 with simple math.

import math
import re


def is_mul_of_15(num: int) -> bool:
    """
    check if num is multiples of 15.

    :param num: the integer to check
        the integer must not be larger than 100.
    """
    for i in range(1, math.ceil(100/15)+1):
        if num == i * 15:
            return True
            break
    return False


def fb() -> None:
    """
    Prints the required FizzBuzz
    """
    for i in range(1, 101):
        s = str(i)
        if is_mul_of_15(i):
            print("FizzBuzz")
        elif re.search('[05]$', s):
            print("Buzz")
            continue
        elif sum((int(digit) for digit in s)) % 3 == 0:
            print("Fizz")
        else:
            print(i)


def main() -> None:
    fb()


if __name__ == '__main__':
    main()
