// FizzBuzz with DataFrame
// @MuhamadAzizi

import pandas as pd
import numpy as np

df = pd.DataFrame(
        {
            'Number': np.arange(100)
        }
    )

for i in df['Number']:
    if i % 3 == 0 and i % 5 == 0:
        df.replace({'Number' : i}, 'FizzBuzz', inplace=True)
    elif i % 3 == 0:
        df.replace({'Number' : i}, 'Fizz', inplace=True)
    elif i % 5 == 0:
        df.replace({'Number' : i}, 'Buzz', inplace=True)

pd.set_option('display.max_rows', None)

print(df)
