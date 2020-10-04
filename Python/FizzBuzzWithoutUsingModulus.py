# FizzBuzz Without using modulus operator (%)
# Author: @gahan9


def reminder_finder(number, divisor=3):
    if number < divisor:
        return number
    reminder = reminder_finder(number, divisor << 1)
    if reminder >= divisor:
        return reminder - divisor
    return reminder


print(*("Fizz" * (reminder_finder(i, 3) == 0) + "Buzz" * (reminder_finder(i, 5) == 0) or str(i) for i in range(1, 101)))
