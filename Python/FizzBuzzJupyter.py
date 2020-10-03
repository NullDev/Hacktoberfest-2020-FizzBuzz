#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
x = np.arange(1,101)


# In[12]:


for i in x:
    if np.mod(i,3) == 0:
        print("Fizz")
    elif np.mod(i,5) == 0:
        print("Buzz")
    elif np.mod(i,3) == 0 and np.mod(i,5) == 0:
        print("FizzBuzz")
    else: print(i)    


# In[ ]:




