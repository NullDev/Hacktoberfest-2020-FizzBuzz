; ==============================================================================
;   File . . . . . . recursive_fizzbuzz.au3
;   Author . . . . . CreepSore
;   Last Edit. . . . 2020-10-01 07:50
;   Description. . . Implements a recursive method for the FizzBuzz Problem
;                    See: https://github.com/NLDev/Hacktoberfest-2020-FizzBuzz
; ==============================================================================

Func FizzBuzz($num)
	$res = ""

	If Mod($num, 3) = 0 Then
		$res &= "Fizz"
	EndIf

	If Mod($num, 5) = 0 Then
		$res &= "Buzz"
	EndIf

	if StringLen($res) = 0 Then
		$res = $num
	EndIf

	ConsoleWrite($res & @CRLF)

	if $num < 100 Then
		FizzBuzz($num + 1)
	EndIf
EndFunc

FizzBuzz(1)
