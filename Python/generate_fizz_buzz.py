# Generate another python script with handcoded fizz buzz rules
# and then execute the file
# author : @rishabhvarshney14

import os

def create_file(start=1, end=100):
    with open('fizzbuzzfile.py', 'w') as f:
        f.write(f'for i in range({start}, {end + 1}):\n')
        for i in range(start, end+1):
            if i % 3 == 0 and i % 5 == 0:
                if i == start:
                    f.write(f'\tif i == {i}: print("FizzBuzz")\n')
                else:
                    f.write(f'\telif i == {i}: print("FizzBuzz")\n')
            elif i % 3 == 0:
                if i == start:
                    f.write(f'\tif i == {i}: print("Fizz")\n')
                else:
                    f.write(f'\telif i == {i}: print("Fizz")\n')
            elif i % 5 == 0:
                if i == start:
                    f.write(f'\tif i == {i}: print("Buzz")\n')
                else:
                    f.write(f'\telif i == {i}: print("Buzz")\n')
            else:
                if i == start:
                    f.write(f'\tif i == {i}: print("{i}")\n')
                else:
                    f.write(f'\telif i == {i}: print("{i}")\n')

create_file()

os.system('python fizzbuzzfile.py')