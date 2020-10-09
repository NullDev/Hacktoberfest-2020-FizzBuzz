#n
# This is a standalone implementation of FizzBuzz using only sed, without hardcoding the print statements.
# Author: @PAndaContron

# The first line (#n) is necessary for sed to disable auto-print.
# If it's not there, it prints out an extra line before it quits.

# Because of the way sed works, the script needs a file with at least one character in it.
# It doesn't matter what file you use; you can actually run this file on itself for convenience.
#     sed -f FizzBuzzStandalone.sed FizzBuzzStandalone.sed
# This script works on both GNU sed and POSIX versions of sed like those found on MacOS and BSD.

# The actual input isn't relevant, so we replace it with a string that we'll use to keep track of the current program.
# The first token is the current number mod 3,
# the second token is the current number mod 5,
# and the third token is the current number.
# The first 2 tokens are suffixed with T and F respectively so that they can be pattern matched more easily.
s/^.*$/1T 1F 1/

:loop
    # Copy the current state into the hold space for backup
    h

    # Check if the current number is divisible by 3
    /0T/{
        # Check if the current number is divisible by 5
        /0F/{
            # Print "FizzBuzz", then restore the state from the hold space
            s/.*/FizzBuzz/
            p
            g
        }

        # Check if the current number is not divisible by 5
        /[^0]F/{
            # Print "Fizz", then restore the state from the hold space
            s/.*/Fizz/
            p
            g
        }
    }

    # Check if the current number is not divisible by 3
    /[^0]T/{
        # Check if the current number is divisible by 5
        /0F/{
            # Print "Buzz", then restore the state from the hold space
            s/.*/Buzz/
            p
            g
        }

        # Check if the current number is not divisible by 5
        /[^0]F/{
            # Print the number, then restore the state from the hold space
            s/.* //
            p
            g
        }
    }

    # If the number was 100, quit
    /100$/q

    # Now we use pattern matching to increment the index.
    # To prevent incrementing the index twice, the new state is stored in the hold space,
    # while the pattern space always contains the old state.
    # (If we didn't do this, we'd replace 0 with 1, then 1 with 2,... until we got to 9 every time)
    # Keep in mind that at the beginning of this segment, the hold space and pattern space are equal.

    # If the number ends in 0, change the last digit to a 1
    /0$/{
        s/0$/1/
        x
    }

    # If the number ends in 1, change the last digit to a 2
    /1$/{
        s/1$/2/
        x
    }

    # If the number ends in 2, change the last digit to a 3
    /2$/{
        s/2$/3/
        x
    }

    # If the number ends in 3, change the last digit to a 4
    /3$/{
        s/3$/4/
        x
    }

    # If the number ends in 4, change the last digit to a 5
    /4$/{
        s/4$/5/
        x
    }

    # If the number ends in 5, change the last digit to a 6
    /5$/{
        s/5$/6/
        x
    }

    # If the number ends in 6, change the last digit to a 7
    /6$/{
        s/6$/7/
        x
    }

    # If the number ends in 7, change the last digit to a 8
    /7$/{
        s/7$/8/
        x
    }

    # If the number ends in 8, change the last digit to a 9
    /8$/{
        s/8$/9/
        x
    }

    # If the number ends in 9, we need to edit 2 digits

    # If the number is just a 9, change it to 10
    / 9$/{
        s/ 9$/ 10/
        x
    }

    # If the number ends in 19, change the last 2 digits to 20
    /19$/{
        s/19$/20/
        x
    }

    # If the number ends in 29, change the last 2 digits to 30
    /29$/{
        s/29$/30/
        x
    }

    # If the number ends in 39, change the last 2 digits to 40
    /39$/{
        s/39$/40/
        x
    }

    # If the number ends in 49, change the last 2 digits to 50
    /49$/{
        s/49$/50/
        x
    }

    # If the number ends in 59, change the last 2 digits to 60
    /59$/{
        s/59$/60/
        x
    }

    # If the number ends in 69, change the last 2 digits to 70
    /69$/{
        s/69$/70/
        x
    }

    # If the number ends in 79, change the last 2 digits to 80
    /79$/{
        s/79$/80/
        x
    }

    # If the number ends in 89, change the last 2 digits to 90
    /89$/{
        s/89$/90/
        x
    }

    # If the number ends in 99, change it to 100
    # This doesn't work for numbers over 100 that end in 99, but it doesn't have to because we're only going up to 100.
    /99$/{
        s/99$/100/
        x
    }

    # Copy the state from the hold buffer back to the pattern buffer
    g

    # Now we need to update the mod values.
    # Instead of actually calculating the modulus, we just use separate counters that wrap around modulo 3 and 5 respectively.
    # We use the same method as before, keeping the old state in the pattern space to avoid incrementing multiple times.

    # Update mod 3 counter
    /0T/{
        s/0T/1T/
        x
    }
    /1T/{
        s/1T/2T/
        x
    }
    /2T/{
        s/2T/0T/
        x
    }

    # Copy the new state back into the pattern space
    g

    # Update mod 5 counter
    /0F/{
        s/0F/1F/
        x
    }
    /1F/{
        s/1F/2F/
        x
    }
    /2F/{
        s/2F/3F/
        x
    }
    /3F/{
        s/3F/4F/
        x
    }
    /4F/{
        s/4F/0F/
        x
    }

    # Copy the new state back into the pattern space
    g

    # Branch back to the top of the loop
    b loop
