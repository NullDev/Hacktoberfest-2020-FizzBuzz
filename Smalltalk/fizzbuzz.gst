"Fizzbuzz Program in Smalltalk language. Install gnu-smalltalk package to run the file"
"Author: @sumitpore"

1 to: 100 do: [:x |

            output:= x.
            
            (x \\ 3 == 0) ifTrue: [
		        output:= 'Fizz'
        	].
        	
        	(x \\ 5 == 0) ifTrue: [
        	    (output == 'Fizz') 	ifTrue: [ output:= 'FizzBuzz' ]
					ifFalse: [ output:= 'Buzz' ]
        	].
        	
        	output printNl.
]