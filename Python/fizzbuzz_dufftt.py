# Trying FizzBuzz.
# Author @dufftt


def fizzBuzz(n):
  for number in range(n):
      if number % 3 == 0:
          print("FizzBuzz" if number % 5 == 0 else "Fizz")
          continue
      print("Buzz" if number % 5 == 0 else number)
      
fizzBuzz(101)
