// [A slightly modified recursive implementation of fizzbuzz]
// Author: @Vishant93
import java.util.Scanner;

public class FizzBuzzModifiedRecursion {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        String res = fizzBuzzRec(1, n);
        System.out.println(res);
    }
    public static String fizzBuzzRec(int i, int n) {
        if (i == n) return i + " ";
        else if (i % 15 == 0) return "FizzBuzz " + fizzBuzzRec(i+1,n);
        else if (i % 5 == 0) return "Buzz " + fizzBuzzRec(i+1,n);
        else if (i % 3 == 0) return "Fizz " + fizzBuzzRec(i+1,n);
        else return i + " " + fizzBuzzRec(i+1, n);
    }
}
