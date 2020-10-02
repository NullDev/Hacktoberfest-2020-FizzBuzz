function fizzBuzz2(n) {
  for (let i = 1; i <= n; i++) {
    let str = "";

    if (i % 3 === 0) str += "fizz"
    if (i % 5 === 0) str += "buzz"
    if (str === "") str = i;
  
    console.log(str);
  }
}


for (var i = 1; i < 101; i++) {
	if (i % 15 == 0) console.log("FizzBuzz");
	else if (i % 3 == 0) console.log("Fizz");
	else if (i % 5 == 0) console.log("Buzz");
	else console.log(i);
}

for(let i = 1; i <= 100; i++) {
  output = ""
  if(i % 3 == 0) {
    output += "Fizz"
  }
  if(i % 5 == 0) {
    output += "Buzz"
  }
  console.log(output)
}
