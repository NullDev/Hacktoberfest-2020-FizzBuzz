def fizz_buzz_generator(fizzbuzz, start=1, end=21):

  """ Prints all of the answers for fizz, buzz or fizzbuzz between the specified interval"""

  def fizz(start, end):
    for i in range(start,end):
      if i % 3 == 0:
        yield f"{i} : 'FIZZ!'"

  def buzz(start, end):
      for i in range(start,end):
        if i % 5 == 0:
          yield f"{i} : 'BUZZ!'"

  def fizz_buzz(start, end):
      for i in range(start,end):
        if i % 5 == 0 and i % 3 == 0:
          yield f"{i} : 'FIZZBUZZ!'"


  if fizzbuzz == 'fizz' :
    try :
      x = fizz(start, end)
      for i in range(start, end):
        print(next(x))
    except StopIteration:
      pass

  if fizzbuzz == 'fizzbuzz' :
    try:
      x = fizz_buzz(start, end)
      for i in range(start, end):
        print(next(x))
    except StopIteration:
      pass

  if fizzbuzz == 'buzz' :
    x = buzz(start, end)
    try:
      for i in range(start, end):
        print(next(x))
    except StopIteration:
      pass

# Test it yourself :
# fizz_buzz_generator(start=0, end = 1000, fizzbuzz='buzz')
