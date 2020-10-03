# 1s are the only means to create primitives!
# Author: @rangolucas

for n in range(1, ((1 + 1 + 1)**(1 + 1) + 1)**(1 + 1) + 1):
    line = str()
    if not n % (1 + 1 + 1):
        F = chr(int(str(((1 + 1 + 1)**(1 + 1) + 1)**(1 + 1) + (1 + 1 + 1)*(1 + 1)), (1 + 1)**(1 + 1 + 1)))
        i = chr(int(str(1) + str(1 + 1 + 1 + 1 + 1) + str(1), (1 + 1)**(1 + 1 + 1)))
        zz = chr(((1 + 1 + 1)**(1 + 1) + 1 + 1)**(1 + 1) + 1)*(1 + 1)
        line += F + i + zz
    if not n % (1 + 1 + 1 + 1 + 1):
        B = chr(((1 + 1 + 1)**(1 + 1) + 1 + 1)*(1 + 1 + 1)*(1 + 1))
        u = chr(((1 + 1 + 1)**(1 + 1) + 1 + 1)**(1 + 1) - 1 - 1 - 1 - 1)
        zz = chr(int(str(1) + str(1 + 1) + str(1 + 1)))*(1 + 1)
        line += B + u + zz
    print([line, n][line == str()])
