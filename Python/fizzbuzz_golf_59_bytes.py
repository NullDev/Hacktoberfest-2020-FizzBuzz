# Fizzbuzz code golf 59 bytes version 1
# Author: @ntsd
i=1
while i<101:print('FizzBuzz'[i%-3&4:12&8-i%5]or i);i+=1
