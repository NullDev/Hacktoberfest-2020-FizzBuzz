// Test Driven Development version of FuzzBuzz
// Author: @Alesnim
// Co-Author: @pr1metine
package fizzbuzz.tdd;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.stream.IntStream;
import java.util.stream.Stream;

@DisplayName("Test for FuzzyBuzzy task")
public class TestExample {

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
  @ValueSource(ints = { 0, 200, Integer.MAX_VALUE, Integer.MIN_VALUE })
  public void testWithoutBounds(Integer x) {
    Assertions.assertEquals(Integer.toString(x), FizBuzzTDD.fizzBuzz(x));
  }

}