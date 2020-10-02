// Groovy v2.4.8 code to print FizzBuzz (Fizz for multiples of three, Buzz for multiples of 5, FizzBuzz for multiples of both 3 and 5 (i.e., multiples of 15) )

class FizzBuzz {

   static void main(String[] args) {

        def lowerLimit = 1, upperLimit = 100;    // Setting the limits for output

        for (int i = lowerLimit; i <= upperLimit; i++) {
            if (i%3==0) {
                if (i%5==0) println "FizzBuzz";
                else println "Fizz";
            }
            else if (i%5==0) println("Buzz");
            else println(i);
        }

   }

}