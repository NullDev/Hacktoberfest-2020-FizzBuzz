<?php 
// PHP program to print Fizz Buzz 

$i; 
for ($i = 1; $i <= 100; $i++) 
{ 
	// number divisible by 3 and 
	// 5 will always be divisible 
	// by 15, print 'FizzBuzz' in 
	// place of the number 
	if ($i % 15 == 0) 
		echo "FizzBuzz" . " "; 
	
	// number divisible by 3? print 
	// 'Fizz' in place of the number 
	else if (($i % 3) == 0) 
		echo "Fizz" . " ";			 
	
	// number divisible by 5, print 
	// 'Buzz' in place of the number 
	else if (($i % 5) == 0)				 
		echo "Buzz" . " ";			 

	else // print the number		 
		echo $i," " ;			 
} 


?> 
