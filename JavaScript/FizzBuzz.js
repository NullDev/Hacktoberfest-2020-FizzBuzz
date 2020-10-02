var i, values = [, , 'fizz', , 'buzz', 'fizz', , , 'fizz', 'buzz', , 'fizz', , , 'fizzbuzz'];

for (i = 0; i < 100; console.log(values[i++ % 15] || i));