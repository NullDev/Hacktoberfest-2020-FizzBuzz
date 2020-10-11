' FizzBuzz in VBA with Excel
' Author: @cnguyen-uk

Sub FizzBuzz()
    Columns("A").HorizontalAlignment = xlCenter  ' Nicely center align the result column
    For i = 1 To 100
        If (i Mod 15) = 0 Then
            Cells(i, 1) = "FizzBuzz"
        ElseIf (i Mod 5) = 0 Then
            Cells(i, 1) = "Buzz"
        ElseIf (i Mod 3) = 0 Then
            Cells(i, 1) = "Fizz"
        Else
            Cells(i, 1) = i
        End If
    Next
End Sub
