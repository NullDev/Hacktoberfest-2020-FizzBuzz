// Easiest implementation of FizzBuzz in Kotlin with JUnit Test
// Test file name - fizzBuzz-ram-test.kt
// Author: @ramkrishnan6

fun fizzBuzz(number: Int): Any {
    return if (number % 15 == 0) "FizzBuzz"
    else if (number % 3 == 0) "Fizz"
    else if (number % 5 == 0) "Buzz"
    else number
}
