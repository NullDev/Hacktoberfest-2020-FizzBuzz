' FizzBuzz in VBA with Outlook
' Author: @cnguyen-uk

Sub FizzBuzz()
    ' The following creates a new email for the output FizzBuzz result.
    Dim objApp As Object
    Dim newMail As MailItem
    Set objApp = Outlook.Application
    Set newMail = objApp.CreateItem(olMailItem)

    For i = 1 To 100
        If (i Mod 15) = 0 Then
            newMail.Body = newMail.Body & "FizzBuzz"
        ElseIf (i Mod 5) = 0 Then
            newMail.Body = newMail.Body & "Buzz"
        ElseIf (i Mod 3) = 0 Then
            newMail.Body = newMail.Body & "Fizz"
        Else
            newMail.Body = newMail.Body & i
        End If
    Next

    newMail.Display  ' Show the output FizzBuzz result
End Sub
