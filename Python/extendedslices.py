# interesting way using python extended slices
# Author: @hwennnn

# More information on extended slices at https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

# First, we initialise the array with range of 0..100
# Wait, you may be asking why include 0? Hold on and keep reading!
# Let's take a look at the example below

# >>> arr = range(10) ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> arr[::2]
# [0, 2, 4, 6, 8]

# arr[::2] means it will jump to the respective index from the first element by 2!
# Therefore, we have to start at 0 and if not, everything will go wrong. We could just simply skip the first index when printing the output later.

# The remaining step is rather obvious by modifying the value based on the number and index.
# And finally, we print them out!

arr = [i for i in range(101)]

arr[::3] = ['Fizz'] * len(arr[::3])
arr[::5] = ['Buzz'] * len(arr[::5])
arr[::15] = ['FizzBuzz'] * len(arr[::15])

print("\n".join(map(str, arr[1:])))