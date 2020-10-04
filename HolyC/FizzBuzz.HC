// This is the only FizzBuzz solution God accepts
// See PR for more information: https://github.com/NLDev/Hacktoberfest-2020-FizzBuzz/pull/508
// Author: @Azgeb

U0 Main(){
    I8 *fizz = "Fizz";
    I8 *buzz = "Buzz";
    I64 iterations = 100;
    for(i = 1; i <= iterations; i++){
        I8 fizzOrBuzz = 0;
        if(i % 3 == 0){
            Print(fizz);
            fizzOrBuzz = 1;
        }
        if(i % 5 == 0){
            Print(buzz);
            fizzOrBuzz = 1;
        }
        if(fizzOrBuzz == 0){
            "d%", i;
        }
        "\n";
    }

    "\n";
    "\n";
    "\n";
    "________________";
    "| Made by Azgeb|";
    "________________";
    "/n";
}

Main();
