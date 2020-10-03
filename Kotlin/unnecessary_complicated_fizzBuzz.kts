// An unnecessarily complicated script to solve fizzbuzz
// Author: @Sironheart

fun main() {
    var myFutureFinishedStringToReturnAOutput: String = ""
    val allTheValuesWeWantToSearchIn: IntRange = 1..100
    for (theCurrentValueWeCheck in allTheValuesWeWantToSearchIn){
        val theCurrentValueWeCheckIsFizz: Boolean = checkIfValueIsFizz(theCurrentValueWeCheck.toInt())
        val theCurrentValueWeCheckIsBuzz: Boolean = checkIfValueIsBuzz(theCurrentValueWeCheck)
        val theCurrentValueWeCheckIsFizzBuzz: Boolean = checkIfValueIsFizzBuzz(theCurrentValueWeCheck)

        myFutureFinishedStringToReturnAOutput += if (theCurrentValueWeCheckIsFizzBuzz) "FizzBuzz" else if (theCurrentValueWeCheckIsBuzz) "Buzz" else if (theCurrentValueWeCheckIsFizz) "Fizz" else theCurrentValueWeCheck.toString()
        myFutureFinishedStringToReturnAOutput += "\r\n"
    }

    print(myFutureFinishedStringToReturnAOutput)
}

fun checkIfValueIsFizz(toCheckValueForFizz: Int): Boolean {
    when {
        toCheckValueForFizz % 3 == 0 -> return true
        toCheckValueForFizz % 3 == 1 -> return false
        toCheckValueForFizz % 3 == 2 -> return false
        toCheckValueForFizz % 3 == 3 -> return false
        else -> return false
    }
    return false
}

fun checkIfValueIsBuzz(toCheckValueForBuzz: Int): Boolean {
    when {
        toCheckValueForBuzz % 5 == 0 -> return true
        toCheckValueForBuzz % 5 == 1 -> return false
        toCheckValueForBuzz % 5 == 2 -> return false
        toCheckValueForBuzz % 5 == 3 -> return false
        toCheckValueForBuzz % 5 == 4 -> return false
        toCheckValueForBuzz % 5 == 5 -> return false
        else -> return false
    }
    return false
}

fun checkIfValueIsFizzBuzz(toCheckValueForFizzBuzz: Int): Boolean {
    when {
        toCheckValueForFizzBuzz % 5 == 0 && toCheckValueForFizzBuzz % 3 == 0 -> return true
        toCheckValueForFizzBuzz % 5 == 0 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 0 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 0 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        toCheckValueForFizzBuzz % 5 == 1 && toCheckValueForFizzBuzz % 3 == 0 -> return false
        toCheckValueForFizzBuzz % 5 == 1 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 1 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 1 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        toCheckValueForFizzBuzz % 5 == 2 && toCheckValueForFizzBuzz % 3 == 0 -> return false
        toCheckValueForFizzBuzz % 5 == 2 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 2 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 2 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        toCheckValueForFizzBuzz % 5 == 3 && toCheckValueForFizzBuzz % 3 == 0 -> return false
        toCheckValueForFizzBuzz % 5 == 3 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 3 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 3 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        toCheckValueForFizzBuzz % 5 == 4 && toCheckValueForFizzBuzz % 3 == 0 -> return false
        toCheckValueForFizzBuzz % 5 == 4 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 4 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 4 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        toCheckValueForFizzBuzz % 5 == 5 && toCheckValueForFizzBuzz % 3 == 0 -> return false
        toCheckValueForFizzBuzz % 5 == 5 && toCheckValueForFizzBuzz % 3 == 1 -> return false
        toCheckValueForFizzBuzz % 5 == 5 && toCheckValueForFizzBuzz % 3 == 2 -> return false
        toCheckValueForFizzBuzz % 5 == 5 && toCheckValueForFizzBuzz % 3 == 3 -> return false
        else -> return false
    }
    return false
}