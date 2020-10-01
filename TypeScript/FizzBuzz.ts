
class FizzBuzz {
    constructor() {}
    public solveFizzBuzzProblem(n: number): void {
        // loop from 1 till the number
      for (let i = 1; i <= n; i++) {
          // check if the current iterator value is divisible by both 3 or 5, print FizzBuzz
          // if only divisible by 3, print Fizz
          // if only divisible by 5, print Buzz
          // else print the iterator itself
        if (i % 3 === 0 && i % 5 === 0) console.log("FizzBuzz");
        else if (i % 3 === 0) console.log("Fizz");
        else if (i % 5 === 0) console.log("Buzz");
        else console.log(i);
      }
    }
  }
  
  // driver code
  const obj = new FizzBuzz();
  obj.solveFizzBuzzProblem(17);

  