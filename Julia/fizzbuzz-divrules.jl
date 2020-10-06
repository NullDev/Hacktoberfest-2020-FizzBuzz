#!/usr/bin/julia
# FizzBuzz using basic division rules
# Author: @joaogui1

function div3(n)
    s = string(n)
    while length(s) > 1
        s = string(sum([parse(Int, c) for c in s]))
    end
    return s in ["0", "3", "6", "9"]  
end

function div5(n)
    s = string(n)
    return s[end] in "05"   
end

function fizzbuzz(n)
    for i = 1:n
        print(i, ": ")
        by3, by5 = div3(i), div5(i)
        
        if by3 && by5
            println("FizzBuzz")
        elseif by3
            println("Fizz")
        elseif by5
            println("Buzz")
        else
            println(i)
        end
    end
end


fizzbuzz(100)
