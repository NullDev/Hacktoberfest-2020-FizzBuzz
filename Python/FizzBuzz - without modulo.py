# An approach to solve FizzBuzz without using modulo operator
# Author: @cyberGhoulK

def if_divisible_by_3(num: int):
  num = str(num)
  while len(num) != 1:
    s = sum(map(int, num))
    num = str(s)
  return int(num) in [3, 6, 9]

def if_divisible_by_5(num: int):
  return int(str(num)[-1]) in [0, 5]

print("\n".join(map(str, [('Fizz'*(if_divisible_by_3(num)) + 'Buzz'*(if_divisible_by_5(num)) or num) for num in range(1, 101)])))
