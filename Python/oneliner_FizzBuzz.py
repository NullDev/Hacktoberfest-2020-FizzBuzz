import numpy as np
print(list(map(lambda x:x[:4] if len(x)<=6 else x,list(np.char.add(np.array(list(map(lambda x:"Fizz" if x%3==0 else "",range(1,101))),dtype=np.str),np.array(list(map(lambda x:"Buzz" if x%5==0 else x,range(1,101))),dtype=np.str))))))
