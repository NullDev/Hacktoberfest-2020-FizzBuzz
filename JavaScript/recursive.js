// Nobody likes Loops. Recursive is better!
// Author: @jonas32


function fizzbuzz(num, limit) {
    if(num % 3 === 0 && num % 5 === 0){
        console.log("FizzBuzz")
    }else if(num % 3 === 0) {
        console.log("Fizz")
    }else if(num % 5 === 0){
        console.log("Buzz")
    }else{
        console.log(num)
    }
    if(num < limit){
        fizzbuzz(num+1, limit);
    }
}

fizzbuzz(0, 100)
