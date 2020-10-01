// Simple FizzBuzz using Kotlin "Range" and "when" control flow 
// Author: @mohitDeshpande

fun main() {
  for (i in 1..100) {
    val fizz = i % 3 == 0
    val buzz = i % 5 == 0
    when {
      fizz && buzz -> println("FizzBuzz")
      fizz -> println("Fizz")
      buzz -> println("Buzz")
      else -> println(i)
    }
  }
}
