//FizzBuzz problem solved with the while loop
//Author: @rootnarayan
let num = 0
while (num++ < 100) {
    console.log(`${num % 3 ? (num % 5 ? num : "Buzz") : num % 5 ? "Fizz" : "FizzBuzz"}`)
}