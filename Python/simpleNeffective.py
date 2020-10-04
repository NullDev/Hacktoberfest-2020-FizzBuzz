#simply good
#Author: @ravish0007


n = 1
while n <= 101:
  answer = []
  if not n%3 :
      answer.append("Fizz")
  if not n%5 :
      answer.append("Buzz")
  print(n if not answer else ''.join(answer))
  n+=1
