#!/usr/bin/julia

function start(n)
    for i = 1:n
        if i % 15 == 0
            print("Fizz-Buzz ")
        elseif i % 3 == 0
            print("Fizz ")
        elseif i % 5 == 0
            print("Buzz ")
        else
            print(i, " ")
        end
        if i % 10 == 0
            println()
        end
    end
end

@time start(100)
