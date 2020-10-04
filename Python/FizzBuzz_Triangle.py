
def printPascal(n) : 
	
	for line in range(0, n) : 
		for i in range(0, line + 1) : 
			print(binomialCoeff(line, i), 
				" ", end = "") 
		print() 

def fizzbuzz(n):
	if n%15 == 0:
		return "FB"
	elif n%3 == 0:
		return "F"
	elif n%5 == 0:
		return "B"
	else:
		return n
	
def binomialCoeff(n, k) : 
	res = 1
	if (k > n - k) : 
		k = n - k 
	for i in range(0 , k) : 
		res = res * (n - i) 
		res = res // (i + 1) 
	
	return fizzbuzz(res) 
 
n = int(input())
printPascal(n) 

# Output for n = 7
'''
1  
1  1  
1  2  1  
1  F  F  1  
1  4  F  4  1  
1  B  B  B  B  1  
1  F  FB  B  FB  F  1 
''' 


