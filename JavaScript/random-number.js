function startFizzBuzz() {
   console.log(fizzBuzzCheck(Math.floor(Math.random() * 100)));
}

function fizzBuzzCheck(number) {
   if (number === 0) {
      return `${number} == Nope`;

   } else if (number % 15 === 0) {
      return `${number} == FizzBuzz`;

   } else if (number % 3 === 0) {
      return `${number} == Fizz`;

   } else if (number % 5 === 0) {
      return `${number} == Buzz`;

   } else {
      return `${number} == Nope`;
   }
}

setInterval(startFizzBuzz, 800);
