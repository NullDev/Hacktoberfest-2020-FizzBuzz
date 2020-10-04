 /*
 Author : Antonio Ferrer Lopez
 Tweeter : @ToniFerrerLopez
 This is my first KATA in java, I prepared it with the intention of practicing TDD with some partners.
 The truth is that it is nothing to write home about but I really enjoyed doing it.
 */

  public class AFL_FizzBuzz_FirstTDD {
     private static final int FIRST_NUMBER = 0;
     private static final int LAST_NUMBER = 100;

     public static void main(String[] args) {
         FizzBuzz fizzBuzz = new FizzBuzz();

         for(int number = FIRST_NUMBER ; number<= LAST_NUMBER ; number++){
             System.out.println("Numero : " + number + " RESPUESTA : " + fizzBuzz.play(number) );
         }
     }

     public static class FizzBuzz {
         public String play(int number) {
             String value = "";
             if (number == 0) value = "ZERO";
             if(number == 1) value = "ONE";
             if(number == 2) value = "TWO";
             if(isDivisibleBythree(number) && isGreaterThanTwo(number)) value = "FIZZ";
             if(isDivisibleByFive(number) && isGreaterThanTwo(number)) value = "BUZZ";
             if(isDivisibleByFive(number) && isDivisibleBythree(number) && isGreaterThanTwo(number)) value = "FIZZBUZZ";
             return value;
         }

         private boolean isDivisibleByFive(int number) {
             return number % 5 == 0;
         }

         private boolean isDivisibleBythree(int number) {
             return number % 3 == 0;
         }

         private boolean isGreaterThanTwo(int number) {
             return number > 2;
         }
     }
 }



 /*SUM OF KATA  :
  * 1 - We have from 1 to 100 like entry point
  * 2- If number is in range of 0 to 2 returns the number name on string format
  * 2 - If Number is divisible by 3 returns FIZZ
  * 3. If number is divisible by 5 returns BUZZ
  * 4. If number is divisible by 3 and 5 return FIZZBUZZ
  * */

 class FizzBuzzTest {
 import org.junit.jupiter.api.BeforeAll;
         import org.junit.jupiter.api.Test;
         import static org.junit.jupiter.api.Assertions.*;


     private static AFL_FizzBuzz_FirstTDD.FizzBuzz fizzBuzz;

     @BeforeAll
     static void beforeAll() {
         fizzBuzz = new AFL_FizzBuzz_FirstTDD.FizzBuzz();
     }

     @Test
     void ifNumberIsZeroShouldReturnZero() {
         String actual = fizzBuzz.play(0);
         assertEquals("ZERO" , actual);
     }

     @Test
     void ifNumberIsOneShouldReturnOne() {
         String actual = fizzBuzz.play(1);
         assertEquals("ONE" , actual);
     }
     @Test
     void ifNumberIs2ShouldReturnTwo() {
         String actual = fizzBuzz.play(2);
         assertEquals("TWO" , actual);
     }
     @Test
     void ifNumberIs3ShouldReturnFizz() {
         String actual = fizzBuzz.play(3);
         assertEquals("FIZZ" , actual);
     }
     @Test
     void ifNumberIs5ShouldReturnBuzz() { ;
         String actual = fizzBuzz.play(5);
         assertEquals("BUZZ" , actual);
     }
     @Test
     void ifNumberIsDivisibleBy3ShouldReturnFizz() {
         String actual = fizzBuzz.play(6);
         assertEquals("FIZZ" , actual);
     }
     @Test
     void ifNumberIsDivisibleBy5ShouldReturnBuzz() {
         String actual = fizzBuzz.play(10);
         assertEquals("BUZZ" , actual);
     }

     @Test
     void ifNumberIsDivisibleBy5AndBy3ShouldReturnFizzBuzz() {
         String actual = fizzBuzz.play(15);
         assertEquals("FIZZBUZZ" , actual);
     }
 }