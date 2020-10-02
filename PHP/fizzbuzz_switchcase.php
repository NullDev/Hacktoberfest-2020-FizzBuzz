<?php

/**
 * Author: mnsora
 * An example of FizzBuzz using switch case
 */

for($i = 1;$i <= 100;$i++){
    switch(true) {
        // current value is multiple of 3 and 5
        case ($i%3 == 0 && $i%5 == 0):
          echo "FizzBuzz"."\n";
            break;
            
        // current value is multiple of 3 only
        case ($i%3 == 0):
          echo "Fizz"."\n";
            break;
        
        // current value is multiple of 5 only
        case ($i%5 == 0):
          echo "Buzz"."\n";
            break;
            
        // others
        default:
            echo $i."\n";
    }
}