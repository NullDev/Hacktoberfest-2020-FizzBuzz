// [JS solution using combination of for loop and if else statements]
// Author: @madarsbiss

const fizzbuzz = (n) => {
	const returnedArr = [];
	for (let i = 1; i <= n; i++) {
		let str = "";
		if (!(i % 3)) str += "Fizz";
		if (!(i % 5)) str += "Buzz";
		if (!str.length) returnedArr.push(i);
		else returnedArr.push(str);
	};
	return returnedArr;
};
