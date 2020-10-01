// Solution using switch statement
// Author: @devashrlucas

for (var i = 1; i < 101; i++) {
  switch (true) {
    case i % 3 == 0:
      console.log("Fizz");
      break;
    case i % 5 == 0:
      console.log("Buzz");
      break;
    case i % 3 == 0:
    case i % 5 == 0:
      console.log("FizzBuzz");
      break;
    default:
      console.log(i);
      break;
  }
}
