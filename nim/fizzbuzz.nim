# FizzBizz!

proc checkSound(i: int, n: int): bool =
  if i mod n == 0:
    return true
  else:
    return false

let sounds: array[3, tuple] = [
  (3, "Fizz"),
  (5, "Buzz"),
  (7, "Bazz")
]

for i in 1 .. 100:
  var output: string = ""
  var a_sound: bool = false
  for sound in sounds:
    if checkSound(i, sound[0]):
      output = output & sound[1]
      a_sound = true
  if a_sound:
    echo output
  else:
    echo i
