let c = 2
let total = 100
while c < 100
  let c += 1
  if c % 3 == 0 && c % 5 != 0
    echom "Fizz"
  elseif c % 5 == 0 && c % 3 != 0
    echom "Buzz"
  elseif c % 15 == 0
    echom "FizzBuzz"
  else
    echom c
  endif
endwhile
