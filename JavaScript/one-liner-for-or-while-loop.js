// A neat JavaScript one-liner to solve FizzBuzz using for or while loop.
// We have a loop that goes from 0 to 100. And within our for loop we are attempting to console.log 'Fizz', 'Buzz' or 'FizzBuzz'
/*
   Breaking Down The Solution:-
   
   for (let i=0; i<100;){
     console.log(
       // First incrementing the i.
       // Then Using ternary operator checking the multiples of 3, 5, or 3 and 5.
       // If i is multiple of 3, then the ternary will return 'Fizz'.
       // If i is multiple of 5, then the ternary will return 'Buzz'.
       // If i is multiple of 3 and 5, then adding two ternary will return 'FizzBuzz'.
       // If not the multiple of both 3 and 5 then LHS of || will become ''(falsy), then the logical operator will return the i.
       (++i % 3 ? '' : 'Fizz') + (i % 5 ? '' : 'Buzz') || i
     )
   }
   
*/
// Author: @neontuts


// Using For Loop
for(let i=0;i<100;)console.log((++i%3?'':'Fizz')+(i%5?'':'Buzz')||i);

// Using While Loop
// let i=0;while(i<100)console.log((++i%3?'':'Fizz')+(i%5?'':'Buzz')||i);

