' FizzBuzz in VBA with Word
' Author: @cnguyen-uk

Sub FizzBuzz()
    For i = 1 To 100
        If (i Mod 15) = 0 Then
            ActiveDocument.Content.InsertAfter Text:="FizzBuzz" & vbCrLf
        ElseIf (i Mod 5) = 0 Then
            ActiveDocument.Content.InsertAfter Text:="Buzz" & vbCrLf
        ElseIf (i Mod 3) = 0 Then
            ActiveDocument.Content.InsertAfter Text:="Fizz" & vbCrLf
        Else
            ActiveDocument.Content.InsertAfter Text:=i & vbCrLf
        End If
    Next
End Sub
