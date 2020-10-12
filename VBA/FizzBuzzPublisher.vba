' FizzBuzz in VBA with Publisher
' Author: @cnguyen-uk

Sub FizzBuzz()
' This subroutine assumes that it is being run in a new publication.

    ' The following sets the page to be 3 inches wide by 30 inches high.
    With ActiveDocument.PageSetup
        .PageWidth = 3 * 72
        .PageHeight = 30 * 72
    End With

    ' The following creates a new textbox of the right size for the output FizzBuzz result.
    Dim objPg As Page
    Dim objSh As Shape
    Set objPg = ActiveDocument.Pages(1)
    Set objSh = objPg.Shapes.AddTextbox(pbTextOrientationHorizontal, 50, 50, 100, 2100)

    For i = 1 To 100
        If (i Mod 15) = 0 Then
            Application.ActiveDocument.Pages(1).Shapes(1).TextFrame.TextRange.InsertAfter "FizzBuzz" & vbCrLf
        ElseIf (i Mod 5) = 0 Then
            Application.ActiveDocument.Pages(1).Shapes(1).TextFrame.TextRange.InsertAfter "Buzz" & vbCrLf
        ElseIf (i Mod 3) = 0 Then
            Application.ActiveDocument.Pages(1).Shapes(1).TextFrame.TextRange.InsertAfter "Fizz" & vbCrLf
        Else
            Application.ActiveDocument.Pages(1).Shapes(1).TextFrame.TextRange.InsertAfter i & vbCrLf
        End If
    Next

    ActiveDocument.ActiveView.Zoom = 100  ' Set zoom level to 100%
End Sub
