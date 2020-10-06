// [Elegant JS solution using array-fill-map]
// Author: @maadrsbiss

const fizzbuzz = n => Array(n).fill().map((e, i) => {
	i++;
	return `${i % 3 ? "" : "Fizz"}${i % 5 ? "" : "Buzz"}` || i;
});
