<?php

// An unnecessarily complicated script to solve fizzbuzz
// Author: @Scarwolf

$myFunnyWannabeArrayString = "";

for ($i = 1; $i <= 100; $i++) {
    $myFunnyWannabeArrayString .= ($i === 1) ? '[' : '';
    $myFunnyWannabeArrayString .= ($i !== 100 ? $i . ',' : $i . ']');
}

$myArray = explode(',', $myFunnyWannabeArrayString);

// It may be unnecessarily complicated but at least you can add any values you like here
$whatIShouldReturnIfIDivideByTheKeyAndTheOnlyThingLeftIsZero = [
    3   => "Fizz",
    5   => "Buzz",
    15  => "FizzBuzz",
];
$myArrayWithFizzesAndBuzzes = [];

for($x = 1; $x <= count($myArray); $x++) {
    $value = $x;

    for($i = 0; $i < count($whatIShouldReturnIfIDivideByTheKeyAndTheOnlyThingLeftIsZero); $i++) {
        if($x % array_keys($whatIShouldReturnIfIDivideByTheKeyAndTheOnlyThingLeftIsZero)[$i] === 0) {
            $value = array_values($whatIShouldReturnIfIDivideByTheKeyAndTheOnlyThingLeftIsZero)[$i];
        }
    }
    $myArrayWithFizzesAndBuzzes[] = $value;
}


for ($i = 0; $i !== count($myArrayWithFizzesAndBuzzes); $i++) {
    echo $myArrayWithFizzesAndBuzzes[$i]; echo '<br>';
}
