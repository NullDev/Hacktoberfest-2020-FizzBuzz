// Another way of writing fizzBuzz using javascript basic array methods(map, reduce)
// Author: @hwennnn

// Notes:
// The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.
// The reduce() method executes a reducer function (that you provide) on each element of the array, resulting in single output value.

// First, we reduce each value in the array to an output which is first initialised as ""
// In this step, each value will loop through the dictionary(which has the number and the word respectively) and append word to the output if it meets the condition 
// (let's say, it will append 3 to the output if it is divisible by 3 and so on)
// However, there will be some value in the arr which would not meet the requirement, meaning the value is not divisible by either 3 or 5;
// and the output will be just "" which we initialised at the first.
// Therefore, we need to map those values back to the integer (with map function, we can get the index for each value in the array)
// Finally, we print out the value!

function FizzBuzz(length, dict) {
    var arr = [];
    for (var i = 1; i <= length; i++) { arr.push(i) }

    arr.map(val => {
            return dict.reduce((output, object) => {
                if (val % object.number === 0) {
                    output += object.word;
                }
                return output;
            }, "");
        })
        .map((output, idx) => {
            return output == "" ? (idx + 1) : output;
        })
        .forEach(val => {
            console.log(val);
        });
}

FizzBuzz(100, [{ number: 3, word: "Fizz" }, { number: 5, word: 'Buzz' }])