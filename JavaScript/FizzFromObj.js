// Fizzbuzz from array of objects
// Author: @Loeka1234

console.log(
	Array(100)
		.fill({ 3: "Fizz", 5: "Buzz" })
		.map((a, i) =>
			Object.keys(a).map((k, j) =>
				(j === 0 ? ++i : i) % k === 0 ? a[k] : i
			)
		)
		.map((a, i) =>
			a.some(v => typeof v === "string")
				? a.filter(v => typeof v === "string").join("")
				: ++i
		)
		.join(", ")
);