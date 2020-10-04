setInterval(startTime, 1000);

function startTime() {
   const now = new Date();
   let hour = now.getHours() < 10 ? `0${now.getHours()}` : now.getHours();
   let minute = now.getMinutes() < 10 ? `0${now.getMinutes()}` : now.getMinutes();
   let second = now.getSeconds() < 10 ? `0${now.getSeconds()}` : now.getSeconds();

   const time = `${hour} : ${minute} : ${second}`;
   const fizzBuzz = `${fizzBuzzCheck(now.getHours())} : ${fizzBuzzCheck(now.getMinutes())} : ${fizzBuzzCheck(now.getSeconds())}`;

   console.log(time);
   console.log(fizzBuzz + "\n");
}

function fizzBuzzCheck(number) {
   if (number === 0) {
      return "Nope";

   } else if (number % 15 === 0) {
      return "FizzBuzz";

   } else if (number % 3 === 0) {
      return "Fizz";

   } else if (number % 5 === 0) {
      return "Buzz";

   } else {
      return "Nope";
   }
}