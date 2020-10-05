// function to print fizz for multiples of 3 and buzz in multiples of 5 and fizzbuzz for multiples of both 3 and 5
// Author: @Rushil9

import java.util.List;
import java.util.ArrayList;

public class FizzBuzz {
    public static List<String> fizzBuzz(int n) {
        List<String> lt = new ArrayList<>();
        String str = "";
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 != 0) {
                lt.add("Fizz");
            }
            if (i % 5 == 0 && i % 3 != 0) {
                lt.add("Buzz");
            }
            if (i % 3 == 0 && i % 5 == 0 && i != 1) {
                lt.add("FizzBuzz");
            }
            if (i % 3 != 0 && i % 5 != 0) {
                lt.add(Integer.toString(i));
            }

        }
        return lt;
    }

    public static void main(String[] args) {
        String out = String.join("\n", fizzBuzz(100));
        System.out.println(out);
    }
}
