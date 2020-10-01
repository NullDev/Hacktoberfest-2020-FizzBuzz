// FizzBuzz in scala
// Author: emilkovacev

object FizzBuzz {
  def main(args: Array[String]): Unit = {
    val A = 3  // multiple: Fizz
    val B = 5  // multiple: Buzz

    def fizzBuzzCalc(value: Int): String = {
      var retVal = ""

      if (value % A == 0) retVal += "Fizz"
      if (value % B == 0) retVal += "Buzz"
      retVal
    }

    for (i <- 1 to 100) println(if (fizzBuzzCalc(i).isEmpty) i else fizzBuzzCalc(i))
  }
}