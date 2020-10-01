<?php
// A fizzbuzz script written in PHP using the recursive method
// Author: @KMuthusamyms

function fizz($n){
    if ($n==101)
        return 0;
    if ($n%3 == 0 && $n%5 == 0)
        echo "FizzBuzz <br>";
    else if ($n%5 == 0)
       echo "Buzz ";
    else if (n%3 == 0)
       echo "Fizz <br>";
    else
        echo $n. '<br>';
    return fizz($n+1);
}

fizz(1);

?>
