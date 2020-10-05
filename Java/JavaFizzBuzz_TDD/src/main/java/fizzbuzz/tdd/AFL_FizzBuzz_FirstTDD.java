// This is my first KATA in java, I prepared it with the intention of practicing TDD with some partners.
// The truth is that it is nothing to write home about but I really enjoyed doing it.
// Author : Antonio Ferrer Lopez
// Tweeter : @ToniFerrerLopez
// Co-Author: @pr1metine
package fizzbuzz.tdd;

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
