/**
 * Implementation of FizzBuzz using StringBuilder
 * 
 * @author Rana M. Suleman
 */
public class FizzBuzz_StringBuilder {

    public static void main(String[] args) {
        fizzBuzz(15);
    }

    public static void fizzBuzz(int n) {

        for (int i = 1; i <= n; i++) {

            StringBuilder str = new StringBuilder();

            if (i % 3 == 0)
                str.append("fizz");

            if (i % 5 == 0)
                str.append("buzz");

            if (str.length() == 0)
                System.out.println(i);
            else
                System.out.println(str);

        }
    }
}
