// elegant way using array index
// Author: @hwennnn

// The code actually did explain everything.

function FizzBuzz() {
    for (i = 0; ++i < 101;) {
        console.log([i, "Fizz", "Buzz", "FizzBuzz"][!(i % 3) + !(i % 5) * 2])
    }
}

FizzBuzz();