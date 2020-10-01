# Description: An implementation using iterator
# @Author: Oxel40


class FizzBuzzIterator:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n > 100:
            raise StopIteration
        out = ""
        if self.n % 3 == 0:
            out += "Fizz"
        if self.n % 5 == 0:
            out += "Buzz"
        if not len(out) > 0:
            out = str(self.n)
        self.n += 1
        return out


if __name__ == "__main__":
    for e in FizzBuzzIterator():
        print(e)
