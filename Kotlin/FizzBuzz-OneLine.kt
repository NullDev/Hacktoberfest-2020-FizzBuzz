// Kotlin in one line
// Author: @veotani
fun main(args: Array<String>) { println(((1..100).map{ if (it % 15 == 0) "FizzBuzz" else if (it % 3 == 0) "Fizz" else if (it % 5 == 0) "Buzz" else it.toString()}).joinToString(separator = "\n")) }