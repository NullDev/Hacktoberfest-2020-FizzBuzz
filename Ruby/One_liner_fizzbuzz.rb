# Fizzbuzz solved in one line and less charcters with ruby tenary operator
# Author: @mihrab34

def fizz_buzz(int)
  1.upto(int) { |val| puts val % 15 ==0 ? 'FizzBuzz': val % 5 == 0 ? 'Buzz': val % 3 ==0 ? 'Fizz': val }
end