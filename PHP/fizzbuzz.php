<?php 

//A short php script to solve fizzbuzz
// Author: @Tooxic

for ($i = 1; $i <= 100; $i++) {
    if ($i % 15 == 0) {
        echo 'FizzBuzz<br>';
    } elseif ($i % 3 == 0) {
        echo 'Fizz<br>';
    } elseif ($i % 5 == 0) {
        echo 'Buzz<br>';
    } else {
        echo $i . '<br>';
    }
}

?>