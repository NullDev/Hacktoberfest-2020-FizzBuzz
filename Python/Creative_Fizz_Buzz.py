
answer=[]

def fizz_buzz(start,end):
    for i in range(start,end+1):
    
        if i%3==0 and i%5==0:
            answer.append('FizzBuzz')
        elif i%3==0:
            answer.append('Fizz')
        elif i%5==0:
            answer.append('Buzz')
        else:
            answer.append(str(i))

    return answer

answer=fizz_buzz(1,100)
for i in range(len(answer)):
    if answer[i].isdecimal():
        print(answer[i]) 
    else:
        print(f'{answer[i]}({i+1})')

    
