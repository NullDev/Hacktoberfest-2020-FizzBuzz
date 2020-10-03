// FizzBuzz Using Functions in Bash
// Author: @Vibe30

#!/bin/bash

x=0
Fizzbuzz() { (! (( x % 3 )) ) && (! ((x % 5)) ) && echo "Fizzbuzz"; }
Fizz()  { (! (( $x % 3 )) ) && echo "Fizz"; }
Buzz()  { (! (( $x % 5 )) ) && echo "Buzz"; }


while ((x < 101 ))
do

Fizzbuzz $x || Fizz $x || Buzz $x || echo $x

((x++))
done
