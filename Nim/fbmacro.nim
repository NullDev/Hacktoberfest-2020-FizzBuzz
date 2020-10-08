import macros

macro fb(i : untyped) : untyped =
    result = newStmtList()
    for j in 0..<i.intVal:
        if j mod 15 == 0:
            result.add(nnkCommand.newTree(ident("echo"), newLit("FizzBuzz")))
        if j mod 3 == 0:
            result.add(nnkCommand.newTree(ident("echo"), newLit("Fizz")))
        if j mod 5 == 0:
            result.add(nnkCommand.newTree(ident("echo"), newLit("Buzz")))
        else:
            result.add(nnkCommand.newTree(ident("echo"), newLit(j)))

fb(101)
