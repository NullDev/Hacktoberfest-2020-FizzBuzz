// FizzBuzz in Scala using recursion
// Author: @mbaldassarri


object FizzBuzz extends App {
  
  def playGame(n: Int):Any = {
      if (n < 101) {
        println(check(n))
        playGame(n + 1)
      }
    }

  def check(n: Int) =  {
    if (n % 3 == 0 && n % 5 != 0) "Fizz"
    else if (n % 5 == 0 && n % 3 != 0) "Buzz"
    else if (n % 3 == 0 && n % 5 == 0) "FizzBuzz"
    else n
  }

  playGame(1)
}
