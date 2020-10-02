# runs perfectly
# Here are the functions:
def alpha2alpha(num):	### function 1
    if num%(((255+(-200)+3)/2-2)/9)==((277/4*0-81*16*0)/(1000*22)):
        return True
def beta2beta(num):	#function 2
    if num%((975/15*2-5)/25)==((621/4*0-211*99*0)/(855*63)):
        return True
def alpha2beta(num):	### function 3
    if num%((9999/33*2-6)/(22*2/4*3+7))==((455/66*0-522*765*0)/(111*22)):
        return True
  
##### main program is here
for i in range (1,101):
    if alpha2beta(i):
        print("FizzBuzz")
    elif alpha2alpha(i):
        print("Fizz")
    elif beta2beta(i):
        print("Buzz")
    else:
        print(i)