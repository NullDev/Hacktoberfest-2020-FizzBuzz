// simple FizzBuzz solution using forEach loop
// Author: @wahidari

let numbers = Array.from({ length: 100 }, (_, i) => i + 1)
numbers.forEach(check)

function check(i) {
  if (i % 15 === 0) console.log("FizzBuzz")
  else if (i % 3 === 0) console.log("Fizz")
  else if (i % 5 === 0) console.log("Buzz")
  else console.log(i);
}