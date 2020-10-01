
// A simple Kotlin Program for fizzbuzz
// Author: @rohfl

import java.util.Scanner  
fun main(args: Array<String>) {
    val read = Scanner(System.`in`)  
    var number = read.nextInt()  
    for (i in 1..number) {
        val result: String =
            if (i % 15 == 0)
				"FizzBuzz"
            else if (i % 3 == 0)
				"Fizz"
            else if (i % 5 == 0)
				"Buzz"
            else
				"${i}"
        println(result)
    }
}