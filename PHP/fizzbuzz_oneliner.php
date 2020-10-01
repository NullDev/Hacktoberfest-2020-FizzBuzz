<?php

// FizzBuzz One liner Using PHP 7.4 Arrow functions & nested ternary operators
// Author: @Scarwolf

foreach (array_map(fn($v) => !($v % 15) ? "FizzBuzz" : (!($v % 5) ? "Buzz" : (!($v % 3) ? "Fizz" : $v)), range(1, 100)) as $value) { echo $value . '<br>'; }
