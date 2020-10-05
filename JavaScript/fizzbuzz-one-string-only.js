function generateFizzy(){
    let base = "";
    for (i = 0; i <= 100; ++i) {
        if (i %15 === 0) {
            base += "FizzBuzz\n"
        }
        else if (i % 5 === 0){
            base += "Buzz\n"
        }
        else if ( i% 3 === 0) {
            base += "Fizz\n"
        }
        else {
            base += i
            base += "\n"
        }
    }
    return base
}

console.log(generateFizzy())
