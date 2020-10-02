// Do While FizzBuzzz
// Author: @gh0sttttt

let i = 0;
do {
  i++;
  if (i % 3 === 0 && i % 5 === 0) {
    console.log('FizzBuzz');
  } else if (i % 5 === 0) {
    console.log('Buzz');
  } else if (i % 3 === 0) {
    console.log('Fizz');
  } else {
    console.log(i);
  }
} while (i < 100);

