# Author: @carol975
# Given a string with "fizz" and "buzz"s, print all possible combinations of numbers
# that generate the string
# When "fizzbuzz" is considered as a whole word, 15 is used to represent this word

def reverse_fizz_buzz(s):
    if not s:
        return [""]
    combos = []

    child_combos = reverse_fizz_buzz(s[4:])
    for child in child_combos:
        if s[:4] == 'fizz':
            combos.append("3," + child)
        elif s[:4] == 'buzz':
            combos.append("5," + child)

    if s[:8] == 'fizzbuzz':
        child_combos = reverse_fizz_buzz(s[8:])
        for child in child_combos:
            combos.append("15," + child)
    return combos

combos = reverse_fizz_buzz("fizzbuzzfizzbuzzbuzzfizz")
print(combos)
# ['3,5,3,5,5,3,', '3,5,15,5,3,', '15,3,5,5,3,', '15,15,5,3,']
        