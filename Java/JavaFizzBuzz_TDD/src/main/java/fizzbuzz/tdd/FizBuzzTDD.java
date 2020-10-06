// Test Driven Development version of FuzzBuzz
// Author: @Alesnim
// Co-Author: @pr1metine
package fizzbuzz.tdd;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FizBuzzTDD {
    /*
     * public static void main(String[] args) { Scanner scanner = new
     * Scanner(System.in); fizzBuzz(scanner.nextInt());
     * 
     * }
     */

    /*
     *
     * First version. All test failed
     *
     * public static String fizzBuzz(int x){ return ""; }
     *
     */

    /*
     * Second version. Test FizzBuzz test failed. public static String fizzBuzz(int
     * x) { if (x % 3 == 0) return "Fizz"; else if (x % 5 == 0) return "Buzz"; else
     * return "FizzBuzz"; }
     */

    /*
     * Third version. Border cases failed. Doesn't check range input data.
     *
     * public static String fizzBuzz(int x) { if ((x % 3 == 0) && (x % 5 == 0))
     * return "FizzBuzz"; if (x % 3 == 0) return "Fizz"; if (x % 5 == 0) return
     * "Buzz"; return ""; }
     */

    /*
     * Fourth version. All test passed, but if number not Fuzz, not Buzz and not
     * FuzzBuzz, function not returned value. Rewrite tests.
     *
     * public static String fizzBuzz(int x) { if (x > 0 && x <= 100) { if ((x % 3 ==
     * 0) && (x % 5 == 0)) return "FizzBuzz"; if (x % 3 == 0) return "Fizz"; if (x %
     * 5 == 0) return "Buzz"; } return ""; }
     */

    public static String fizzBuzz(int x) {
        if (x > 0 && x <= 100) {
            if ((x % 3 == 0) && (x % 5 == 0))
                return "FizzBuzz";
            if (x % 3 == 0)
                return "Fizz";
            if (x % 5 == 0)
                return "Buzz";
        }
        return String.valueOf(x);

    }
}
