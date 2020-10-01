// My fizzBuzzSolution | Hacktoberfest-2020-FizzBuzz
// Author: @ZachyDev

// define an empty array
const arr = [];

// iterate from 1 - 100
for(let i = 1; i < 100; i++) {
    // update the arr
    arr.push(i);
}

// using array helper: forEach,check the conditions
arr.forEach(elem => {
    return (
        elem % 3 == 0 ? console.log('Fizz') :
        elem % 5 == 0 ? console.log('Buzz') :
        elem % 3 == 0 && elem % 5 == 0 ? console.log('FizzBuzz') :
        console.log(elem)
    );
});