# Description: A oneliner for FizzBuzz using generators. (No lambda or map)
# @Author: Oxel40

print(*[o if j % 5 != 0 else "Buzz" if len(str(o)) < 4 else o+"Buzz" for (j, o) in [(i, a if i % 3 != 0 else "Fizz") for (i, a) in [(x, x) for x in range(1, 101)]]], sep='\n')
