//FizzBuzz using recursive in TypeScript
//Author : iamshubhankarkhare

function fizzbuzz(num: number, limit:number) {
  console.log((++num%3?'':'Fizz')+(num%5?'':'Buzz')||num)
    if(num < limit){
        fizzbuzz(num+1, limit);
    }
}

fizzbuzz(0, 100)
