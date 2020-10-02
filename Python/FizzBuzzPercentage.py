# Calculates the what percentage of a sentence consist FizzBzz
# Created by @SaaranshM

def fizzbuzz_percentage(s):
    """
    s is the sentence to check
    """

    # initializing the count of fizzbuzz
    fizzbuzz_count = 0

    split_sentence = s.split(" ")
    print(split_sentence)

    for word in split_sentence:
        if word == 'FizzBuzz':
            fizzbuzz_count += 1

    # returns percentage of fizzbuzz in sentence
    return (fizzbuzz_count/len(split_sentence)) * 100

