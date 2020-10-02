import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class FizBuzzTDD {

    public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);
        //fizzBuzz(scanner.nextInt());


    }

    /*
     *
     * First version. All test failed
     *
     * public static String fizzBuzz(int x){
     *    return ""; }
     *
     */


    /*
    * Second version. Test FizzBuzz test failed.
    * public static String fizzBuzz(int x) {
        if (x % 3 == 0) return "Fizz";
        else if (x % 5 == 0) return "Buzz";
        else return "FizzBuzz";
    }*/


    /*
    * Third version. Border cases failed. Doesn't check range input data.
    *
    * public static String fizzBuzz(int x) {
        if ((x % 3 == 0) && (x % 5 == 0)) return "FizzBuzz";
        if (x % 3 == 0) return "Fizz";
        if (x % 5 == 0) return "Buzz";
        return "";
    }*/

    /*
    * Fourth version. All test passed, but if number not Fuzz, not Buzz and not FuzzBuzz,
    * function not returned value. Rewrite tests.
    *
    * public static String fizzBuzz(int x) {
        if (x > 0 && x <= 100) {
            if ((x % 3 == 0) && (x % 5 == 0)) return "FizzBuzz";
            if (x % 3 == 0) return "Fizz";
            if (x % 5 == 0) return "Buzz";
        }
        return "";
    }*/

    public static String fizzBuzz(int x) {
        if (x > 0 && x <= 100) {
            if ((x % 3 == 0) && (x % 5 == 0)) return "FizzBuzz";
            if (x % 3 == 0) return "Fizz";
            if (x % 5 == 0) return "Buzz";
        }
        return String.valueOf(x);

    }
}

@DisplayName("Test for FuzzyBuzzy task")
class TestExample {

    private final String fizz = "Fizz";
    private final String buzz = "Buzz";
    private final String fizzBuzz = "FizzBuzz";


    public static Stream<Integer> fizzy() {
        return IntStream.range(1, 101).filter(i -> (i % 3 == 0) && (i % 5 != 0)).boxed();
    }

    public static Stream<Integer> buzzy() {
        return IntStream.range(1, 101).filter(i -> (i % 5 == 0) && (i % 3 != 0)).boxed();
    }

    public static Stream<Integer> fuzzysBuzzys() {
        return IntStream.range(1, 101).filter(i -> (i % 5 == 0) && (i % 3 == 0)).boxed();
    }

    // Simple test

    @Test
    public void testFizz() {
        Assertions.assertEquals(fizz, FizBuzzTDD.fizzBuzz(3));
    }


    @Test
    public void testBuzz() {
        Assertions.assertEquals(buzz, FizBuzzTDD.fizzBuzz(5));
    }


    @Test
    public void testFizzBuzz() {
        Assertions.assertEquals(fizzBuzz, FizBuzzTDD.fizzBuzz(15));
    }


    @Test
    public void testNothing() {
        Assertions.assertEquals("1", FizBuzzTDD.fizzBuzz(1));
    }


    // Parametrized tests

    @ParameterizedTest
    @MethodSource("fizzy")
    public void testFuzzyAll(Integer x) {
        Assertions.assertEquals(fizz, FizBuzzTDD.fizzBuzz(x));
    }


    @ParameterizedTest
    @MethodSource("buzzy")
    public void testBuzzyAll(Integer x) {
        Assertions.assertEquals(buzz, FizBuzzTDD.fizzBuzz(x));
    }


    @ParameterizedTest
    @MethodSource("fuzzysBuzzys")
    public void testFuzzyBuzzyAll(Integer x) {
        Assertions.assertEquals(fizzBuzz, FizBuzzTDD.fizzBuzz(x));
    }


    // Borderline cases

    @ParameterizedTest
    @ValueSource(ints = {0, 200, Integer.MAX_VALUE, Integer.MIN_VALUE})
    public void testWithoutBounds(Integer x) {
        Assertions.assertEquals(Integer.toString(x), FizBuzzTDD.fizzBuzz(x));
    }


}
