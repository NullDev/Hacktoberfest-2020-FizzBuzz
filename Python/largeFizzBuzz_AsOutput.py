'''A large FizzBuzz as an output using small FizzBuzz numbers.(FizzBuzz=FizBuz for better alignment 
and make sure your output terminal covers the entire length of the screen to avoid automatic newlines)'''
# Author: @AmanMatrix
def iCheck(i):
    if i%15==0:
        i='FizBuz'
    elif i%3==0:
        i='Fizz'
    elif i%5==0:
        i='Buzz'
    else:i=i
    return i
for i in range(1,101):
    if(i==1):
        print("\n",iCheck(i),end=" ")
    elif(i<=5):
        print(iCheck(i),end=" ")
    elif(i==6):
        print("                                          ",iCheck(i),end=" ")
    elif(i<=9):
        print(iCheck(i),end=" ")
    elif(i==10):
        print(f"\n  {iCheck(i)}",end="                ")
    elif(i<=12):
        print(iCheck(i),end="")
    elif(i==13):
        print("                               ",iCheck(i),end="          ")
    elif(i==14):
        print(iCheck(i))
    elif(i==15):
        print(iCheck(i),end="                  ")
    elif(i==16):
        print(iCheck(i),end="                                  ")
    elif(i<=18):
        print(iCheck(i),end="         ")
    elif(i==19):
        print(f"\n  {iCheck(i)}",end="                                                        ")
    elif(i<=21):
        print(iCheck(i),end="       ")
    elif(i==22):
        print(f"\n  {iCheck(i)}",end=" ")
    elif(i<=25):
        print(iCheck(i),end=" ")
    elif(i==26):
        print("   ",iCheck(i),end="")
    elif(i<=27):
        print(iCheck(i),end="   ")
    elif(i==28):
        print(iCheck(i),end=" ")
    elif(i<=30):
        print(iCheck(i),end=" ")
    elif(i==31):
        print("  ",iCheck(i),end=" ")
    elif(i<=33):
        print(iCheck(i),end=" ")
    elif(i==34):
        print(" ",iCheck(i),end=" ")
    elif(i<=36):
        print(iCheck(i),end="")
    elif(i<=37):
        print("      ",iCheck(i),end="")
    elif(i<=38):
        print("     ",iCheck(i),end="")
    elif(i==39):
        print("  ",iCheck(i),end=" ")
    elif(i<=41):
        print(iCheck(i),end=" ")
    elif(i==42):
        print(" ",iCheck(i),end=" ")
    elif(i<=44):
        print(iCheck(i),end=" ")
    elif(i==45):
        print(f"\n{iCheck(i)}",end="                ")
    elif(i<=47):
        print(iCheck(i),end=" ")
    elif(i<=49):
        print("         ",iCheck(i),end="  ")
    elif(i==50):
        print(" ",iCheck(i),end="     ")
    elif(i==51):
        print(" ",iCheck(i),end="   ")
    elif(i==52):
        print(iCheck(i),end="      ")
    elif(i==53):
        print(iCheck(i),end="          ")
    elif(i<=55):
        print(iCheck(i),end="         ")
    elif(i==56):
        print(f"\n  {iCheck(i)}",end="                  ")
    elif(i<=58):
        print(iCheck(i),end="")
    elif(i<=60):
        print("      ",iCheck(i),end="    ")
    elif(i<=61):
        print(" ",iCheck(i),end="          ")
    elif(i<=62):
        print(iCheck(i),end="   ")
    elif(i<=64):
        print(iCheck(i),end="     ")
    elif(i<=66):
        print(iCheck(i),end="          ")
    elif(i<=67):
        print(f"\n  {iCheck(i)}",end="                  ")
    elif(i<=69):
        print(iCheck(i),end="")
    elif(i<=71):
        print("   ",iCheck(i),end="        ")
    elif(i<=72):
        print(" ",iCheck(i),end="        ")
    elif(i<=73):
        print(iCheck(i),end="    ")
    elif(i<=74):
        print(iCheck(i),end="    ")
    elif(i<=75):
        print(iCheck(i),end="  ")
    elif(i<=76):
        print(iCheck(i),end="             ")
    elif(i<=77):
        print(iCheck(i),end="  ")
    elif(i<=78):
        print(f"\n {iCheck(i)}",end="                 ")
    elif(i<=80):
        print(iCheck(i),end="")
    elif(i==81):
        print("  ",iCheck(i),end=" ")
    elif(i<=83):
        print("",iCheck(i),end="")
    elif(i<=84):
        print("    ",iCheck(i),end=" ")
    elif(i<=86):
        print(iCheck(i),end="")
    elif(i<=87):
        print("   ",iCheck(i),end=" ")
    elif(i<=89):
        print(iCheck(i),end=" ")
    elif(i<=90):
        print("    ",iCheck(i),end="")
    elif(i<=92):
        print(iCheck(i),end="")
    elif(i<=93):
        print("  ",iCheck(i),end="")
    elif(i<=95):
        print("",iCheck(i),end="")
    elif(i<=96):
        print("  ",iCheck(i),end="")
    elif(i<=99):
        print(iCheck(i),end="")
    else:
        print(" ",iCheck(i))