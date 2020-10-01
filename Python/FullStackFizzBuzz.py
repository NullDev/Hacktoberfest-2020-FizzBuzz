"""
A full FizzBuzz generator that covers the things you will need to work with FizzBuzz. (I think)

Some examples are included.
"""
# Author: @Arthurdw
from typing import Union, List


class FizzBuzz:
    def __init__(self,
                 fizz: Union[int, str, bool] = "Fizz",
                 buzz: Union[int, str, bool] = "Buzz"):
        """The general FizzBuzz object.

        Args:
            fizz (optional [int, str, bool]): The Fizz value.
            buzz (optional [int, str, bool]): The Buzz value.

        Params:
            current (list [int, str, bool]): A FizzBuzz
        """
        self.fizz = fizz
        self.buzz = buzz
        self.current = list(self.generate(100))

    def __len__(self):
        return len(self.current)

    def __iter__(self):
        return self.generate()

    def __str__(self):
        return self.prep_collection(self.current)

    def __repr__(self):
        return f"<FizzBuzz fizz=\"{self.fizz}\" buzz=\"{self.buzz}\" current=list[{len(self)} items]>"

    @staticmethod
    def prep_collection(collection: List[Union[int, str, bool]], delimiter: str = "\n") -> str:
        """
        Prepare your FizzBuzz collection for a string.

        Args:
            collection (list [int, str, bool]): Your FizzBuzz list.
            delimiter (optional str): The string delimiter. Default is \n (new line)
        """
        return delimiter.join([str(i) for i in collection])

    def generate(self, count: int = 100) -> Union[int, str, bool]:
        """
        Generates the FizzBuzz array

        Args:
            count (int): The range for the FizzBuzz
        """
        for i in range(1, count + 1):
            is_fizz = i % 3 == 0
            is_buzz = i % 5 == 0
            yield self.fizz + self.buzz if is_fizz and is_buzz else\
                self.fizz if is_fizz else self.buzz if is_buzz else i


if __name__ == "__main__":
    print("The normal FizzBuzz")
    print(FizzBuzz())

    print("FizzBuzz but with Hello as Fizz and World as Buzz")
    print(FizzBuzz("Hello", "World"))

    print("The index gets prepended")
    for index, item in enumerate(FizzBuzz().generate()):
        print(index + 1, item)

    print("A collection with all numbers that aren't Fizz, Buzz or FizzBuzz")
    print([item for item in FizzBuzz() if isinstance(item, int)])

    print("Ladder printed FizzBuzz")
    print("\n".join([" " * idx + str(i) for idx, i in enumerate(FizzBuzz())]))
