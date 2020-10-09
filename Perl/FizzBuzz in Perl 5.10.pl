
# FizzBuzz in Perl 5.10

use strict;
use warnings;
use diagnostics;

use 5.10.0;

# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".

for my $n (1..100) {
    # Print word if...
    !($n % 15) ?    say "FizzBuzz"    :   # Divisible by 3 and 5
    !($n % 3)  ?    say "Fizz"        :   # Divisible by 3
    !($n % 5)  ?    say "Buzz"        :   # Divisible by 5
                    say "$n";             # Else just print the number
}
