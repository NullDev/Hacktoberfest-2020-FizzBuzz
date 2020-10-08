This is a macro to be used in the command line (bash) that will open vim and
execute the necessary commands to generate the FizzBuzz sequence.

```
vim -s <(printf "i1 \x1bqqYp\x01q98@qkqqAFizz\x1b3kq32@qGqqABuzz\x1b5kq19@q:%%s/ $\x0d:%%s/^[0-9]* //g\x0d")
```
