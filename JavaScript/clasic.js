// [SHORT DESCRIPTION HERE]
// simplest way to print FizzBuzz with javascript
// Author: @coz-git

// ...

for (i = 0; i < 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        document.write('FizzBuzz', '&nbsp;')
    } else if (i % 3 === 0) {
        document.write('Fizz', '&nbsp;')
    } else if (i % 5 === 0) {
        document.write('Buzz', '&nbsp;')
    } else {
        document.write(i, '&nbsp;')
    }
}
