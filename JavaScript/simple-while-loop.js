// Simple while loop with "else" / "if" and modulus
// Auteur: @EhrenfeldN

function printResult(text_to_display) { console.log(text_to_display); index++; }

let index = 1;

while (index <= 100) {
    if (index % 3 === 0 && index % 5 === 0) printResult("FizzBuzz");
    else if (index % 3 === 0) printResult("Fizz");
    else if (index % 5 === 0) printResult("Buzz");
    else printResult(index);
}
