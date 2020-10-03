#!/usr/bin/julia

function interpreter(n::Int64)
    result = ""
    
    n%3==0 && (result = "Fizz")
    
    n%5==0 && (result *= "Buzz")

    result == "" && (result = n)
    
    return (println(result) ; result) 
end

function fizzBuzzer(limit::Int64 = 100)
    i = 1:limit
    i = map(interpreter, i) 
end

fizzBuzzer()