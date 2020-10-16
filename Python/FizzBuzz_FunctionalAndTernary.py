# My motivation for this solution is a functional approach that is concise
# but still easy to read. For this I combine the functions map, join and
# lambda together with the ternary operator.
# Author: @riwim

print(
    " ".join(
        map(
            lambda i: "FizzBuzz"
            if not i % 15
            else "Fizz"
            if not i % 3
            else "Buzz"
            if not i % 5
            else str(i),
            range(1, 101),
        )
    )
)
