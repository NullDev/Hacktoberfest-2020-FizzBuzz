// FizzBuzz oneliner using nested ternary operator
// Author: @sedlakp
(1...100).forEach { ($0 % (3*5) == 0) ? print("FizzBuzz") : ($0 % 3 == 0) ? print("Fizz") : ($0 % 5 == 0) ? print("Buzz") : print($0) }