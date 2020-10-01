# fizzbuzz program in one line
# Author: @suparna13
print(["FizzBuzz" if number%3 == 0 and number%5 ==0 else ("Fizz" if number%3==0 else ("Buzz" if number%5 == 0 else number)) for number in range(1, 101)])
