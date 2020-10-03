''' here is a simple, shortest and precise code using list comprehension
  Author: @singhankush01'''

l=['fizzbuzz' if i%15==0 else 'fizz' if i%3==0 else 'buzz' if i%5==0 else str(i) for i in range(1,101)]
for i in l:
  print(i)