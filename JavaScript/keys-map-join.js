// [Unique approach using combination of keys, map and join]
// Author: @madarsbiss

const fizzBuzz = () =>
  [...Array(100).keys()]
    .map((_, i) => i + 1)
    .map((i) =>
      i % 3 === 0 && i % 5 === 0
        ? "FizzBuzz"
        : i % 3 === 0
        ? "Fizz"
        : i % 5 === 0
        ? "Buzz"
        : i
    )
    .join("\n");
