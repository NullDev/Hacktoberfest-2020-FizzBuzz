
# Solving fizzbuzz with a finite state machine
# Author : @verebecske

class state_machine:
    def __init__(self):
        self.loop = 0

    def start(self, word: list):
        if word == []:
            print('start: invalid word')
        if word[0] == 0:
            self.k1(word[1:])
        else:
            print('start: invalid word')

    def k1(self, word: list):
        if word == []:
            print('k1: invalid word')
        elif word[0] == 0 or word[0] == 2 or word[0] == 4:
            print(self.loop + 1)
            self.k2(word[1:])
        else:
            print('k1: invalid word')

    def k2(self, word: list):
        if word == []:
            print('k2: invalid word')
        elif word[0] == 0 or word[0] == 2 or word[0] == 3:
            print(self.loop + 2)
            self.c(word[1:])
        elif word[0] == 1:
            print(self.loop + 1)
            self.b(word[1:])
        elif word[0] == 4:
            print(self.loop + 2)
            self.s(word[1:])
        else:
            print('k2: invalid word')

    def c(self, word: list):
        self.loop = self.loop + 3
        if word == []:
            print('Fizz: invalid word')
        elif word[0] == 2 or word[0] == 4:
            print('Fizz')
            self.k1(word[1:])
        elif word[0] == 1:
            print('Fizz')
            self.k2(word[1:])
        elif word[0] == 3:
            print('Fizz')
            self.b(word[1:])
        else:
            print('Fizz: invalid word')

    def b(self, word: list):
        if word == []:
            print('Buzz')
        elif word[0] == 1:
            print('Buzz')
            self.c(word[1:])
        elif word[0] == 3:
            print('Buzz')
            self.k2(word[1:])
        else:
            print('Buzz: invalid word')

    def s(self, word: list):
        self.loop = self.loop + 3
        if word == []:
            print('FizzBuzz: invalid word')
        elif word[0] == 0:
            print('FizzBuzz')
            self.k1(word[1:])
        else:
            print('FizzBuzz: invalid word:')


if __name__ == "__main__":
    word = sorted([0, 1, 2, 3, 4]*3)*7
    machine = state_machine()
    machine.start(word[:100])
