//A neat PHP program to solve FizzBuzz
//Author: @ishika-2302
<?php 
$i; 
for ($i = 1; $i <= 100; $i++) 
{ 
    if ($i % 15 == 0)           //multiple of 15 is both divisible by 3 and 5, thus we printboth fizz+buzz
        echo "FizzBuzz" . "  ";  
  
    else if (($i % 3) == 0)     //multple of 3
        echo "Fizz" . "  ";              
  
    else if (($i % 5) == 0)    //multiple of 5              
        echo "Buzz" . "  ";              
  
    else        
        echo $i,"  " ;              
} 
?> 
