; A FizzBuzz in Autohotkey
; The FizzBuzz prints the output as keystrokes 
; Autor: @Feluin



;  Wait for pressing Space after starting the Script
KeyWait, Space, D 

;The classical Fizzbuzz
Loop, 100 {
	if (Mod(A_Index,  3) == 0 && Mod(A_Index,  5)== 0){
	writeAsKeyInput("Fizzbuzz")
	} else 	if (Mod(A_Index,  3) == 0){
	writeAsKeyInput("Fizz")
	} else 	if (Mod(A_Index,  5) == 0){
	writeAsKeyInput("Buzz")
	} else {
	writeAsKeyInput(A_Index)
	}
	send {Enter}
}

;convert String to Key output
writeAsKeyInput(out){
	string := Format( "{1:s}" , out)
		
	Loop, parse,string
	{
		send  %A_LoopField%
	}
} 