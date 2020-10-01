#Fizzbuzz in Bash
#!/bin/bash
echo "Enter the no."
read a;

  if [ $(( $a%3 )) == 0 ]  && [ $(( $a%5 )) == 0 ]; 
  then echo "fizzbuzz";
  elif [ $(( $a%3 )) == 0 ]; 
  then echo "fizz";
  elif [ $(( $a%5 )) == 0 ]; 
  then  echo "buzz";
  fi
  