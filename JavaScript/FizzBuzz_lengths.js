// My fizzBuzzSolution | Hacktoberfest-2020-FizzBuzz
// Author: @casalazara

let fizz = "Fizz";
let buzz = "Buzz";

// iterate from 1 - 100
for(let i = 1; i < 100; i++) {
    // check the conditions
        if (i % (fizz.length -1)  == 0 && i % (buzz.length + 1) != 0) console.log(fizz);
        else if(i % (buzz.length +1) == 0 && i % (fizz.length -1) != 0) console.log(buzz);
        else if(i % (fizz.length -1) == 0 && i % (buzz.length + 1) == 0) console.log(fizz+buzz)
        else console.log(i);
}


