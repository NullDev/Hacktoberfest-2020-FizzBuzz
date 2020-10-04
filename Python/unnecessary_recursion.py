
def calc_fizzbuzz(n):
    if not (n%3==0 or n%5==0):
        return n

    ret_str = ""
    if n%3==0:
        ret_str += "fizz"
    if n%5==0:
        ret_str += "buzz"
    
    return ret_str


def rec_fizzbuzz(sol):
    n = len(sol) + 1
    if n>100:
        return sol

    item = calc_fizzbuzz(n)
    sol.append(item)
    return rec_fizzbuzz(sol)

def rec_print(sol):
    if sol:
        item = sol.pop()
        rec_print(sol)
        print(item)

sol = []
rec_fizzbuzz(sol)
rec_print(sol)

