#!/bin/bash
# Simple version of FizzBuzz in bash
# Author: @jmmille

for i in {0..100}
do
  if [ $(( $i%3 )) == 0 ]  && [ $(( $i%5 )) == 0 ]; then echo "fizzbuzz";continue;
  elif [ $(( $i%3 )) == 0 ]; then echo "fizz";continue;
  elif [ $(( $i%5 )) == 0 ]; then  echo "buzz";continue;
  fi
  echo $i
done
