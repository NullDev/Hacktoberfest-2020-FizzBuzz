function FizzBuzz(i, n) {
	if(i>n) return(null);
	var str = ''
	str += i%3===0 ? 'Fizz' : ''
	str += i%5===0 ? 'Buzz' : ''
	console.log(str ? str : i)
	FizzBuzz(i+1, n)
}

FizzBuzz(1, 50)
