#!usr/bin/env python3

'''A FizzBuzz script that uses a generator class that doesn't stop at 100,
and also allows arbitary multiple-word triggers.

author: @moltenmuffins
'''

import argparse


class FizzBuzzGenerator:
    """
    A FizzBuzz generator class
    
    Args:
        triggers (list): A list of triggers for number replacement.
            Each trigger is a tuple containing a (multiple, word) pair.
            Defaults to `[(3, "Fizz"), (5, "Buzz")]`.

    Attributes:
        triggers (list): A class attribute storing the list of triggers.
    """

    def __init__(self, triggers=None):
        if triggers is None:
            self.triggers = [
                (3, "Fizz"),
                (5, "Buzz")
            ]
        else:
            self.triggers = triggers
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        i = self.__count

        value = ""
        # Run checks for each trigger
        for (multiple, word) in self.triggers:
            if i % multiple == 0:
                value += word
        # Default to integer if none of the triggers passed
        if not value:
            value = i
        return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, nargs='?', default=100,
                        help="Number of iterations of FizzBuzzGenerator to run")
    args = parser.parse_args()

    print("Starting FizzBuzz...")
    fizz_buzz = FizzBuzzGenerator()
    for i, value in enumerate(fizz_buzz):
        print(value)
        if i >= (args.num - 1):
            break
