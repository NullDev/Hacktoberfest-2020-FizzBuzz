' FizzBuzz in VBA with Access
' Author: @cnguyen-uk

Sub FizzBuzz()
' This subroutine assumes that it is being run in a new database.

    DoCmd.Close  ' Close the automatically opened Table1

    ' The following creates a new table for the output FizzBuzz result.
    Dim dbs As Database
    Dim tbl As TableDef
    Dim fld As Field
    Set dbs = CurrentDb
    Set tbl = dbs.CreateTableDef("FizzBuzz")
    Set fld = tbl.CreateField("Result", dbText)

    tbl.Fields.Append fld
    dbs.TableDefs.Append tbl
    dbs.TableDefs.Refresh

    DoCmd.OpenTable ("FizzBuzz")  ' Open the FizzBuzz table

    DoCmd.SetWarnings False  ' Turn off possible script-interrupting warnings

    For i = 1 To 100
        If (i Mod 15) = 0 Then
            DoCmd.RunSQL "INSERT INTO FizzBuzz (Result) VALUES ('FizzBuzz');"
        ElseIf (i Mod 5) = 0 Then
            DoCmd.RunSQL "INSERT INTO FizzBuzz (Result) VALUES ('Buzz');"
        ElseIf (i Mod 3) = 0 Then
            DoCmd.RunSQL "INSERT INTO FizzBuzz (Result) VALUES ('Fizz');"
        Else
            DoCmd.RunSQL "INSERT INTO FizzBuzz (Result) VALUES (" & CStr(i) & ");"
        End If
    Next i

    DoCmd.SetWarnings True  ' Turn warnings back on for safety

    DoCmd.Requery  ' Refresh database to display the output FizzBuzz result
End Sub
