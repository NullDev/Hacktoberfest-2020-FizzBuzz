'''
I have  used the  Lambda and map functions.
'''
#author:@veldakarimi

print(*map(lambda v: 'Fizz'*(not v%3)+'Buzz'*(not v%5) or v, range(1,101)),sep='\n')
