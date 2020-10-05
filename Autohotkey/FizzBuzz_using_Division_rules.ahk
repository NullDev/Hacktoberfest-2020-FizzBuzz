; Writes out the equation the same way a human would and erases it afterwards
; Author: @EZacS

Space:: ; Click spacebar to Start the script
loop, 100 {
WriteFizzBuzz(A_Index)
}

WriteFizzBuzz(Number) {
	sum := 0
	TempStr := "" + Number
	NumberArray := StrSplit(TempStr)
	Loop % NumberArray.Length() {
		if (A_Index = NumberArray.Length()) {
			send % NumberArray[A_Index]
			send, {Space}{=}{Space}
			Loop % NumberArray.Length() {
				sum := sum + Format("{:d}", NumberArray[A_Index])
			}
			send, %sum%{Enter}
		}
		else {
			send % NumberArray[A_Index]
			send, {Space}{+}{Space}
		}
	}
	if (Divideby3(Number)) {
		send, %Number%{Space}`% 3 {=}{=} 0{Enter}
	}
	Else {
		send, %Number%{space}`% 3 {!}{=} 0{Enter}
	}
	if (Divideby5(A_Index)) {
		send, ends in{Space}
		EndChar := NumberArray[NumberArray.MaxIndex()]
		send % EndChar
		send, {Enter}%EndChar% {=} 0 or 5
	}
	Else {
		send, ends in{Space}
		EndChar := NumberArray[NumberArray.MaxIndex()]
		send % EndChar
		send, {Enter}%EndChar% {!}{=} 0 or 5
	}
	;Sleep, 50
	LoopCount := CharCount(A_Index)
	loop, %LoopCount% {
		send, {BackSpace}
	}
	if (Divideby3(A_Index) and (Divideby5(A_Index))) {
		send, FizzBuzz{Enter}{Enter}
	}
	else if (Divideby3(A_Index)) {
		send, Fizz{Enter}{Enter}
	}
	else if (Divideby5(A_Index)) {
		send, Buzz{Enter}{Enter}
	}
	Else {
		send, %Number%{Enter}{Enter}
	}
	;Sleep, 100
}

Divideby3(Number) {
	sum := 0
	TempStr := "" + Number
	NumberArray := StrSplit(TempStr)
	Loop % NumberArray.Length() {
		sum := sum + Format("{:d}", NumberArray[A_Index])
	}
	if (mod(sum, 3) = 0) {
		Return, True
	}
	Else {
		Return, False
	}
}

Divideby5(Number) {
	TempStr := "" + Number
	NumberArray := StrSplit(TempStr)
	if (NumberArray[NumberArray.Length()] = "0" or NumberArray[NumberArray.Length()] = "5") {
		Return, True
	}
	else {
		Return, False
	}
}

CharCount(Number)  {
	sum := 0
	TempStr := "" + Number
	NumberArray := StrSplit(TempStr)
	Loop % NumberArray.Length() {
		sum := sum + Format("{:d}", NumberArray[A_Index])
	}
	SumStr := StrSplit(sum)
	Var := SumStr.Length() + NumberArray.Length() + 33 + NumberArray.Length() * 4
	if (Divideby5(Number)) {
		Var--
	}
	Return % Var
}
