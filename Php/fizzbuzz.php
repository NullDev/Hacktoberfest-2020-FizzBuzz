<?php
// PHP based solution of fizbuzz solution
// @copy 2020
// Author: @webmidas




function fizzbuzz($range){
	
	$string='';
	
	for ($i = 1; $i <= $range; $i++) 
	{
		if ($i % 5 == 0 && $i % 3 == 0) {
			$string .= "FizzBuzz"."\n";
		} elseif ($i % 3 == 0) {
			$string .= "Fizz"."\n";
		} elseif ($i % 5 == 0) {
			$string .= "Buzz"."\n";
		} else {
			$string .= $i . "\n";
		}
	}
	
	return $string;
	
	
}

//print the output
//echo fizzbuzz(100);

//print the output in a readable way
echo nl2br(fizzbuzz(100));