A version of fizzbuzz in brainfuck with no loops ([]) _ This uses a cell structure as follows [ones][tens][\n][F][i][B][u][z]
Author: @incarnadined

>>>>>>> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 7 to z
< +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 6 to u
< ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 5 B
< +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 4 to i
< ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 3 to F
<++++++++++ Set cell 2 to '\n'
<++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 1 to ASCII 0
<++++++++++++++++++++++++++++++++++++++++++++++++ Set cell 0 to ASCII 0
+. Print 1
>>.<< Print newline
+. Print 2
>>.<< Print newline
>>>.>.>>>..<<<<<<<+ Print Fizz and one to the counter
>>.<< Print newline
+. Print 4
>>.<< Print newline
>>>>>.>.>..<<<<<<<+ Print Buzz and add one to the counter
>>.<< Print newline
>>>.>.>>>..<<<<<<<+ Print Fizz and add one to the counter
>>.<< Print newline
+. Print 7
>>.<< Print newline
+. Print 8
>>.<< Print newline
>>>.>.>>>..<<<<<<<+ Print Fizz and add one to the counter
>>.<< Print newline
--------- Reset cell 0  to 0
>+ Add one to cell 1
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 11 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 13 and newline
.<.+>>.< Print 14 and newline
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 16 and newline
.<.+>>.< Print 17 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 19 and newline
+<----------> Change tens column and reset ones to 0
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 22 and newline
.<.+>>.< Print 23 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 26 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 28 and newline
.<.+>>.< Print 29 and newline
+<----------> Change tens column and reset ones to 0
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 31 and newline
.<.+>>.< Print 32 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 34 and newline
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 37 and newline
.<.+>>.< Print 38 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
+<----------> Change tens column and reset ones to 0
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 41 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 43 and newline
.<.+>>.< Print 44 and newline
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 46 and newline
.<.+>>.< Print 47 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 49 and newline
+<----------> Change tens column and reset ones to 0
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 52 and newline
.<.+>>.< Print 53 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 56 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 58 and newline
.<.+>>.< Print 59 and newline
+<----------> Change tens column and reset ones to 0
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 61 and newline
.<.+>>.< Print 62 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 64 and newline
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 67 and newline
.<.+>>.< Print 68 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
+<----------> Change tens column and reset ones to 0
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 71 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 73 and newline
.<.+>>.< Print 74 and newline
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 76 and newline
.<.+>>.< Print 77 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 79 and newline
+<----------> Change tens column and reset ones to 0
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 82 and newline
.<.+>>.< Print 83 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
.<.+>>.< Print 86 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 88 and newline
.<.+>>.< Print 89 and newline
+<----------> Change tens column and reset ones to 0
>>.>.>>>..<<.>.>..<<<<<<<+>>.< Print FizzBuzz and add one to the counter and new line
.<.+>>.< Print 91 and newline
.<.+>>.< Print 92 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 94 and newline
>>>>.>.>..<<<<<<<+>>.< Print Buzz and add one to the counter and new line
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
.<.+>>.< Print 97 and newline
.<.+>>.< Print 98 and newline
>>.>.>>>..<<<<<<<+>>.< Print Fizz and add one to the counter and new line
>>>>.>.>..<<<<<<<+> Print Buzz
