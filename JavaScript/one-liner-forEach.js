new Array(100).fill(0).forEach(function(value, index){ index++; console.log(index % 3 ? (index % 5 ? index : "Buzz") : index % 5 ? "Fizz" : "FizzBuzz")});

