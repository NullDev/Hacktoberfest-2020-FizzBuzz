<?php

// FizzBuzz One liner Using PHP 7.4 Arrow functions & nested ternary operators
// Author: @Scarwolf

echo implode('<br>', array_map(fn($v) => (!($v % 3) && !($v % 5)) ? "FizzBuzz" : (!($v % 5) ? "Buzz" : (!($v % 3) ? "Fizz" : $v)), range(1, 100)));
