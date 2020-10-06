#!/usr/bin/julia
# FizzBuzz in one line
# Author: @joaogui1

map(println, collect(i % 15 == 0 ? "FizzBuzz" : i % 5 == 0 ? "Buzz" : i % 3 == 0 ? "Fizz" : i for i in 1:100))
