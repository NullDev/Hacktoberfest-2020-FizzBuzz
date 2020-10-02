// Easiest implementation of FizzBuzz in Kotlin with JUnit Test
// Original file name - fizzBuzz-ram.kt
// Author: @ramkrishnan6

import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream
import kotlin.test.assertEquals

class FizzBuzzTest {
    @ParameterizedTest
    @MethodSource
    fun `Number is replaced by its respective string`(number: Int, expected: Any) {
        assertEquals(expected, fizzBuzz(number))
    }

    companion object {
        @JvmStatic
        fun `Number is replaced by its respective string`(): Stream<Arguments> =
                Stream.of(
                        Arguments.of(12, "Fizz"),
                        Arguments.of(333, "Fizz"),
                        Arguments.of(25, "Buzz"),
                        Arguments.of(8950, "Buzz"),
                        Arguments.of(30, "FizzBuzz"),
                        Arguments.of(1515, "FizzBuzz"),
                        Arguments.of(14, 14),
                        Arguments.of(214, 214)
                )
    }
}
