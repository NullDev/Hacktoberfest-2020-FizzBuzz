/* FizzBuzz program  using T-SQL
 Author: @gayatripalkar
 */

DECLARE @FizzBuzz varchar(max) =
    (
    STUFF(
        (SELECT '
' +
            CASE WHEN Id % 15 = 0 THEN 'fizzbuzz'
                WHEN Id % 5 = 0 THEN 'buzz'
                WHEN Id % 3 = 0 THEN 'fizz'
                ELSE CAST(Id AS VARCHAR(5)) END
        FROM (SELECT TOP 1000 ROW_NUMBER() OVER (ORDER BY object_id) Id
                FROM sys.all_columns) FizzBuzz
        ORDER BY Id
        FOR XML PATH, TYPE
    ).value(N'.[1]',N'nvarchar(max)'),1,1,N'')
    );
PRINT @FizzBuzz;