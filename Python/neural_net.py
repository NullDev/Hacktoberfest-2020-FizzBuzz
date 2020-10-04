# A neural net prediction, wont be 100% accurate but watching epochs was fun"
#Author: @ravish0007

import numpy as np



def fizzbuzz(n):
  ans = ''
  if n%3 == 0:
    ans += 'fizz'
  if n%5 == 0:
    ans += 'buzz'
  if ans:
    return ans
  return n

dataset = [ list(map(int, format(i, '#09b')[2:]))  for i in range(1, 101) ]
dataset = [np.array(data).reshape(1,7) for data in dataset ]

classes = {
    'fizz'    :   [0, 0, 0, 1],
     'buzz'   :   [0, 0, 1, 0],
     'fizzbuzz' : [0, 1, 0, 0]
}

outputs =  np.array([ classes.get(fizzbuzz(i), [1,0,0,0])   for i in range(1, 101) ])

# activation function 
  
def sigmoid(x): 
    return(1/(1 + np.exp(-x))) 
    
# Creating the Feed forward neural network 
# 1 Input layer(1, 30) 
# 1 hidden layer (1, 5) 
# 1 output layer(3, 3) 
  
def f_forward(x, w1, w2): 
    # hidden 
    z1 = x.dot(w1)# input from layer 1  
    a1 = sigmoid(z1)# out put of layer 2  
      
    # Output layer 
    z2 = a1.dot(w2)# input of out layer 
    a2 = sigmoid(z2)# output of out layer 
    return(a2) 
   
# initializing the weights randomly 
def generate_wt(x, y): 
    l =[] 
    for i in range(x * y): 
        l.append(np.random.randn()) 
    return(np.array(l).reshape(x, y)) 
      
# for loss we will be using mean square error(MSE) 
def loss(out, Y): 
    s =(np.square(out-Y)) 
    s = np.sum(s)/len(outputs) 
    return(s) 
    
# Back propagation of error  
def back_prop(x, y, w1, w2, alpha): 
      
    # hiden layer 
    z1 = x.dot(w1)# input from layer 1  
    a1 = sigmoid(z1)# output of layer 2  
      
    # Output layer 
    z2 = a1.dot(w2)# input of out layer 
    a2 = sigmoid(z2)# output of out layer 
    # error in output layer 
    d2 =(a2-y) 
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),  
                                   (np.multiply(a1, 1-a1))) 
  
    # Gradient for w1 and w2 
    w1_adj = x.transpose().dot(d1) 
    w2_adj = a1.transpose().dot(d2) 
      
    # Updating parameters 
    w1 = w1-(alpha*(w1_adj)) 
    w2 = w2-(alpha*(w2_adj)) 
      
    return(w1, w2) 
  
def train(x, Y, w1, w2, alpha = 0.01, epoch = 1000): 
    acc =[] 
    losss =[] 
    for j in range(epoch): 
        l =[] 
        for i in range(len(x)): 
            out = f_forward(x[i], w1, w2) 
            l.append((loss(out, Y[i]))) 
            w1, w2 = back_prop(x[i], outputs[i], w1, w2, alpha) 
        print("epochs:", j + 1, "======== acc:", (1-(sum(l)/len(x)))*100)    
        acc.append((1-(sum(l)/len(x)))*100) 
        losss.append(sum(l)/len(x)) 
    return(acc, losss, w1, w2)

w1 = generate_wt(7, 5) 
w2 = generate_wt(5, 4)

acc, losss, w1, w2 = train(dataset, outputs, w1, w2, 0.1, 10000)

def predict(x, w1, w2): 
    Out = f_forward(x, w1, w2) 
    maxm = 0
    k = 0
    for i in range(len(Out[0])): 
        if(maxm<Out[0][i]): 
            maxm = Out[0][i] 
            k = i
    return k

maps = { 
         1: 'fizzbuzz',
         2:'buzz',
         3:'fizz'
    
}
for j,i in enumerate(dataset, start=1):
      print(maps.get(predict(i, w1, w2), j))

