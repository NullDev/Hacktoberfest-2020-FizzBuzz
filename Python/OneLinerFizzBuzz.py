# One liner
# Author: clare0901
print('\n'.join( 'Buzz' * (i % 5 == 0) + 'Fizz' * (i % 3 == 0)  or str(i) for i in range(1, 101) ) )
