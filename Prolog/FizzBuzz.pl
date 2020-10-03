--author: @nchiarappa

divBy3(X) :- 0 is mod(X, 3).
divBy5(X) :- 0 is mod(X, 5).

print_fizz_buzz(X) :- 
    (divBy3(X),divBy5(X))
    	-> write('FizzBuzz') 
    	; divBy3(X) 
    		-> write('Fizz') 
    		; divBy5(X) 
    			-> write('Buzz') 
    			; write(X).

print_numbers(100) :- print_fizz_buzz(100), !.
print_numbers(X) :- print_fizz_buzz(X), nl, Next is X + 1, print_numbers(Next).