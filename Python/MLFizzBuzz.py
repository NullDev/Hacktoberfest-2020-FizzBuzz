# Author: @mzelenetz
"""
The motivation for this solution was based on Joel Grus' Fizz Buzz in Tensorflow Blog Post: https://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/
I wanted to see if I could do something similar with random forests.

We are going to train on 101-2048 then we are going to predict on fizzbuzz from numbers 1-100 
"""

import numpy as np 
from sklearn.ensemble import RandomForestClassifier

# Encodings from Joel Grus' blog
def binary_encode(i, num_digits):
    """
    Encode the features
    """
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizz_buzz_encode(i):
    """
    Encode the labels either Fizzbuzz, Fizz, Buzz, or the number
    """
    if   i % 15 == 0: return np.array([0, 0, 0, 1]) #fizzbuzz
    elif i % 5  == 0: return np.array([0, 0, 1, 0]) #buzz
    elif i % 3  == 0: return np.array([0, 1, 0, 0]) #fizz
    else:             return np.array([1, 0, 0, 0]) #the number

def fizz_buzz(i, prediction):
    """
    Unpack the predictions
    """
    return [str(i), "fizz", "buzz", "fizzbuzz"][prediction]


NUM_DIGITS = 10
X_train = np.array([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])
y_train = np.array([fizz_buzz_encode(i)          for i in range(101, 2 ** NUM_DIGITS)])

X_test = np.array([binary_encode(i, NUM_DIGITS) for i in range(1, 100)])
y_test = np.array([fizz_buzz_encode(i)          for i in range(1, 100)])

# Train the Random Forest
regr = RandomForestClassifier(max_depth=20, random_state=6251)
regr.fit(X_train, y_train)

predicted = regr.predict(X_test)

for i in range(1, 100):
    print(fizz_buzz(i, y_test[i-1].tolist().index(1)))

