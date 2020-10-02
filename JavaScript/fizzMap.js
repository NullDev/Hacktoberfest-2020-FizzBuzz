// FizzBuzzz map function!
// Author: @gh0sttttt

const fizzBuzz = (i, range) => {
  // Declare array
  let fizzyarray = [];
  if (i > -1 && range > i) {
    while (range >= i) {
      // push range of numbers into array
      fizzyarray.push(i);
      i++;
    }
    // Map through the array
    fizzyarray.map(num => {
      num % 3 === 0 && num % 5 === 0 ?
        console.log('FizzBuzz')
        : num % 3 === 0 ?
          console.log('Fizz')
          : num % 5 === 0 ?
            console.log('Buzz')
            :
            console.log(num);

    });
  }
  else {
    console.log('Try entering a valid range of numbers, example : 0-200');
  }
};

fizzBuzz(0, 100);


