// Author: @choijean
// FizzBuzz written in Grace (http://gracelang.org)

for (1 .. 100) do {
    i → if ((i%15)  == 0) then {
        print "FizzBuzz"
    } elseif {
        (i%3)  == 0
    } then {
        print "Fizz"
    } elseif {
        (i%5)  == 0
    } then {
        print "Buzz"
    } else {
        print(i)
    }
} 