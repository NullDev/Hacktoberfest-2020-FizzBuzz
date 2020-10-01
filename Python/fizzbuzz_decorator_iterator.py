# Implementation of fizzbuzz using decorator and iterator
# Author: @jeweljp

class FizzBuzz:
    def __iter__(self):
        self.count = 1
        return self

    def __next__(self):
        if self.count >= 101:
            raise StopIteration
        else:
            if self.count % 5 == 0 and self.count % 3 == 0:
                x = 'FizzBuzz'
            elif self.count % 3 == 0:
                x = 'Fizz'
            elif self.count % 5 == 0:
                x = 'Buzz'
            else:
                x = self.count
            self.count += 1
            return x


def fizzbuzz(func):
    def fizz_buzz():
        my_fizzbuzz = FizzBuzz()
        func(my_fizzbuzz)
    return fizz_buzz


@fizzbuzz
def main(fizz_buzz):
    for element in fizz_buzz:
        print(element)


if __name__ == "__main__":
    main()
