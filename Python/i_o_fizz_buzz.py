"""Fizz buzz pattern in a text file

Each line in the file corresponds to the correct output for that line
number, the line number can never be wrong even if the iterable in
elements in `nums` is unsorted or has negative numbers

Try using this with `nums = range(0, 100, 5)` for instance :D
"""

nums = range(1, 101)
last_num = 1

with open('fizz_buzz.txt', 'w') as f:
    for num in sorted(num for num in nums if num > 0):

        for _ in range(num - last_num):
            print(file=f)

        f.write('FizzBuzz' if not num % 15 else 'Fizz' if not num % 3
                else 'Buzz' if not num % 5 else str(num))
        last_num = num
