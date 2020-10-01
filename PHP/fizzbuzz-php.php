//fizzbuzz php programming
// Author: @Chamudi
<?php
$_fp = fopen("php://stdin", "r");


for($i=1; $i<=100; $i++){
	$check_fizz = $i%3;
	$check_buzz = $i%5;
	$print = "";
	
	if($check_fizz == 0)
		$print .= "Fizz";
	if($check_buzz == 0)
		$print .= "Buzz";
	
	
	if($print == "")
		echo $i;
	else
		echo $print;
	
	echo "\n";
	
}
?>