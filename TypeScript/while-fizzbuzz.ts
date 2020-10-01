// simple fizzbuzz using while loop in typscript
// Author: @dimaswijanarko

function fizzBuzz(a: number) {
  let i: number = 0;
  while (i < a) console.log((++i % 3 ? "" : "Fizz") + (i % 5 ? "" : "Buzz") || i);
}

fizzBuzz(100);
