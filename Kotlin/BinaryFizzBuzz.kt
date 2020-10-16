import kotlin.math.pow
import kotlin.math.roundToInt

fun binaryChecksum(number: Int) : Int {
    var checksum = 0
    for(i in 0 until (32 - number.countLeadingZeroBits()) step 2) {
        checksum += (number shr i and 0b11)
    }
    return checksum
}

fun binaryAlternatingChecksum(number: Int) : Int {
    var checksum = 0
    for((index, i) in (0 until (32 - number.countLeadingZeroBits()) step 2).withIndex()) {
        checksum += (number shr i and 0b11) * (-0b1).toDouble().pow(index).roundToInt()
    }
    return checksum
}

fun main() {
    (1..100).forEach {
        val binaryChecksum = binaryChecksum(it)
        val binaryAlternatingChecksum = binaryAlternatingChecksum(it)

        if(binaryChecksum % 0b11 == 0 && binaryAlternatingChecksum == 0b0) {
            println("FizzBuzz")
        } else if (binaryAlternatingChecksum == 0b0) {
            println("Buzz")
        } else if (binaryChecksum % 0b11 == 0) {
            println("Fizz")
        } else {
            println(it)
        }
    }

}