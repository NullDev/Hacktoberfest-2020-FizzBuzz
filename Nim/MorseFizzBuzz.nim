#[
  Title: MorseFizzBuzz
  Author: @joe733
]#

let Fizz = "..-. .. --.. --.."
let Buzz = "-... ..- --.. --.."

for num in 1..101:
  if num mod 3 == 0 and num mod 5 == 0:
    echo Fizz
  elif num mod 3 == 0:
    echo Buzz
  elif num mod 5 == 0:
    echo Fizz, Buzz
  else:
    echo num
