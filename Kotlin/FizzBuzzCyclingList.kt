//Cycling List
//As 3, 5, 15 have the LCM 15 in common a pre-filled list FizzBuzz representation of range (1..15)
//is enough information for solving the exercise in every bigger range.
//The program below cycles over the pre-filled list
//You can try it online on Kotlin Playground: https://pl.kotl.in/yTZzgpMoZ
//Author: @tobi6112

fun main() {
    val list = listOf<Any?>(null, null, "Fizz", null, "Buzz", "Fizz", null, null, "Fizz", "Buzz", null, "Fizz", null, null, "FizzBuzz")

    (1..100).forEach {
        when(val value = list[(it - 1) % list.size]) {
            is String -> println(value)
            else -> println(it)
        }
    }
}