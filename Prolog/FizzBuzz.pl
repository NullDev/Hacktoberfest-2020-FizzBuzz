/*
Description: A program for FizzBuzz writen in prolog (SWI-Prolog). Call `fizzbuzz().` to start the execution.
@Author: Oxel40
*/

modCheck(N, F, B) :- F is N mod 3, B is N mod 5.

noFizzOrBuzz(NotF, NotB) :- NotF is 1, NotB is 1.

fizzbuzz(101).
fizzbuzz(N) :- modCheck(N, F, B), 
               (F is 0 -> write('Fizz'), NotF is 0 ; NotF is 1), 
               (B is 0 -> write('Buzz'), NotB is 0 ; NotB is 1), 
               (noFizzOrBuzz(NotF, NotB) -> write(N) ; true),
               nl,
               N1 is N+1,
               fizzbuzz(N1).

fizzbuzz() :- fizzbuzz(1).
