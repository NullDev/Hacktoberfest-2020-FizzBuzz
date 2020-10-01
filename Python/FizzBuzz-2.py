# A not so simple Python code to implement FizzBuzz
# Author @InitialPosition


def prime_factorization(number: int):
    # initialize factor array
    prime_factors = []

    # we need to check the entire number range for possible factors
    for x in range(2, number + 1):
        if number % x == 0:
            prime = True

            # actual factor test can terminate at x/2 (+1 for safety)
            for y in range(2, (x // 2 + 1)):
                if x % y == 0:
                    prime = 0
                    break

            # if still flagged, append number to factor array
            if prime:
                prime_factors.append(x)

    return prime_factors


# ebic memes
RESPECT = 'F'
NICE = '69'
MEME = '[B]'

smallest_factors = prime_factorization(4)

word0 = RESPECT + str(bytes.fromhex(NICE))[2] + 2 * str(vars()['prime_factorization'])[23]
word1 = MEME[1] + str(vars()['prime_factorization'])[2] + word0[smallest_factors[0]:smallest_factors[0] * 2]

factorization = prime_factorization(int(RESPECT, 16))

for i in range(100):
    # fix pythons range command
    i += 1

    out = ''

    # very basic loop
    if i % factorization[0] == 0:
        out += word0
    if i % factorization[1] == 0:
        out += word1

    if out == '':
        out = str(i)

    print(out)
