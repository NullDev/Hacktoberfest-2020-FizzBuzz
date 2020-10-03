// a generics class implementation in kotlin
// author : @tomorisakura

fun main(args : Array<String>) {
    // you can change parameter what u want
    val ranges : Range<Any> = Range(100)
    ranges.rangeIt()
}

class Range<T>(val type : T) {
    fun rangeIt() : Any {
        return if (type is Int) {
            for (i in 1..type.toInt()) {
                when {
                    i % 3 == 0 && i % 5 == 0 -> println("FizzBuzz")
                    i % 3 == 0 -> println("Fizz")
                    i % 5 == 0 -> println("Buzz")
                    else -> println(i)
                }
            }
        } else {
            println("opps.. you have wrong input !")
        }
    }
}