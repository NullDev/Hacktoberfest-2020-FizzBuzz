# A minimal way to do FizzBuzz.
# Author @xPolar

for number in range(101):
    if number % 3 == 0:
        print("FizzBuzz" if number % 5 == 0 else "Fizz")
        continue
    print("Buzz" if number % 5 == 0 else number)