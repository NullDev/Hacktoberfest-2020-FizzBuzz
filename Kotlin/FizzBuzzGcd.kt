// Not much different from the standard modulo solution but using the greatest common divisor
// with euclidean Algorithm instead
// You can try it online on Kotlin Playground: https://pl.kotl.in/d37wG8KEB
// Author: @tobi6112

fun gcd(a: Int, b: Int): Int = if(b==0) a else gcd(b, a % b)

fun main() {
    (1..100).forEach {
        when {
            gcd(it, 15) == 15 -> println("FizzBuzz")
            gcd(it, 5) == 5 -> println("Buzz")
            gcd(it, 3) == 3 -> println("Fizz")
            else -> println(it)
        }
    }
}