# StupidFizzBuzz
# Author: @mzelenetz
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

SERIES_LENGTH = 10

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
    ^Idata: Sequence of observations as a list or NumPy array.
    ^In_in: Number of lag observations as input (X).
    ^In_out: Number of observations as output (y).
    ^Idropnan: Boolean whether or not to drop rows with NaN values.
    Returns:
    ^IPandas DataFrame of series framed for supervised learning.
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return '<number>'

def create_input_features(inputs):
    """
    [labels, [features]]
    """
    pad = ['TOKEN'] * SERIES_LENGTH
    for index in range(len(inputs) - SERIES_LENGTH - 1):
        yield [inputs[index], pad + inputs[max(0, index - SERIES_LENGTH ):index]]
        pad = pad[1:]
    

training = [fizzbuzz(num) for num in range(1, 1000)]
training_inputs = list(create_input_features(training))

lb = LabelBinarizer()
lb.fit( training + ['TOKEN'] )


X = np.array([lb.transform(features).flatten() for label, features in training_inputs])
y = np.array([label for label, features in training_inputs])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=6251)


#clf = LogisticRegression(tol=1e-6)
regr = RandomForestClassifier(max_depth=20, random_state=6251)
regr.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
predicted = regr.predict(X_test)
accuracy_score(y_test, predicted)

test = list(create_input_features([num for num in range(1000, 1100)]))

res = []
pad = ['PAD'] * SERIES_LENGTH
input = []
res = []
for i in range(1000, 1101):
    X = lb.transform(pad + input)
    predicted = regr.predict([np.array(X).flatten()])[0]
    if predicted == "<number>":
        res.append(str(i))
    else:
        res.append(predicted)
    input.append(predicted)
    pad = pad[1:]
    if len(input) > SERIES_LENGTH:
        input = input[1:]
