// A typescript buzzy fizz
// Author: @Tolfx

/**
 * 
 * @param amount The amount of times you want to loop
 * @param callback The response
 */
function fizzBuzz(amount: number, callback: (err: null | Error, response: string) => void) {
    for (let i = 0; i < amount; ++i) {
        if (i % 3 === 0 && i % 5 === 0) {
            callback(null, "FizzBuzz");
        } else if (i % 3 === 0) {
            callback(null, "Fizz");
        } else if (i % 5 === 0) {
            callback(null, "Buzz");
        };
    };
}

fizzBuzz(100, (err, response) => {
    if (err) throw err;
    console.log(response);
})