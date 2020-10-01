# FizzBuzz with an accent
# Author: @rgreen324

sero = 0
wan = 1
wanhandredwan = 101
tree = 3
payb = 5

for namber in range(wan, wanhandredwan):
    txt = ''

    if namber % tree == sero:
        txt += 'Piz'

    if namber % payb == sero:
        txt += 'Baz'

    if txt:
        print(txt)
    else:
        print(namber)
