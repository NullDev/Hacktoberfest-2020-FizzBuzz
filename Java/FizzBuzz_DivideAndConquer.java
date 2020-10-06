// Divide and Conquer version of FizzBuzz
// Author: @evamy

import java.util.Arrays;

public class FizzBuzz_DivideAndConquer {

    static void fizzBuzz(int start, int end, String[] outArray) {
        if (start > end) return;
        if (start == end) {
            outArray[start-1] = next(start);
            return;
        }

        int mid = (start+end) / 2;
        fizzBuzz(mid+1, end, outArray);
        fizzBuzz(start, mid, outArray);
    }

    static String next(int num) {
        String ans = "";
        if (num % 3 == 0) ans += "Fizz";
        if (num % 5 == 0) ans += "Buzz";
        if (ans.isEmpty()) ans += num;

        return ans;
    }

    public static void main(String[] args) {
        int n = 100;

        String[] outArray = new String[n];
        fizzBuzz(1, n, outArray);

        System.out.println(Arrays.toString(outArray));
    }

}
