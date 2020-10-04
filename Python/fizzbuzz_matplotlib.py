# A fancy fizzbuzz graph using matplolib
# The output is a png graph showing the 1-100
# numbers in the X-axis and the corresponding
# value 'Fizz', 'Buzz', 'FizzBuzz' in the 
# Y-axis.

# Author: @ecwolf

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True

fizzbuzz_plot = []  # values to be plot
fiz_num = []		# 1-100 values 

##	FizzBuzz = 3
##	Buzz 	 = 2
##	Fizz 	 = 1
##  Normal   = 0 

# fizzbuzz algorithm

for i in range(0,101):
    fiz_num.append(i) 
    if i == 0:
    	fizzbuzz_plot.append(0)
    	continue
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz_plot.append(3)
        continue
    elif i % 3 == 0:
        fizzbuzz_plot.append(1)
        continue
    elif i % 5 == 0:
    	fizzbuzz_plot.append(2)
        continue
    fizzbuzz_plot.append(0)


# Ploting ....

ind = np.arange(len(fiz_num))
fig = plt.figure(figsize=(18,3.5))
ax = fig.add_subplot(111)

ax.plot([p for p in ind], fizzbuzz_plot, color="#AFD2E9" , lw = 2, label="fizzbuzz")

ax.set_xticks(ind)
ax.set_yticks([0,1, 2,3])
ax.set_xticklabels(fiz_num,fontsize=6)

labels = [item.get_text() for item in ax.get_yticklabels()]
labels = ['','Fizz' ,'Buzz' ,'FizzBuzz']
ax.set_yticklabels(labels)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_ticks_position('bottom')

ax.yaxis.grid(linestyle='--')

plt.ylim(ymin=0)
plt.xlim(xmin=0,xmax=100)


# ... output graph

plt.savefig("fizzbuzz_matplotlib.png")

