print(*["fizzbuzz" if (x%3 ==0 and x%5==0) else "fizz" if x%3==0 else "buzz" if x%5==0 else x for x in range(1,101)])
