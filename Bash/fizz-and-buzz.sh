#Fizz and buzz checker in Bash doesn't check directly for fizzbuzz
#!/bin/bash
echo "Enter the number"
read x;

  if [ $(( $x%3 )) == 0 ]; 
  then printf "fizz";
  fi
  if [ $(( $x%5 )) == 0 ]; 
  then echo "buzz";
  fi 
  printf "\n";