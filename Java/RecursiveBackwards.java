public class RecursiveBackwards {
    public static void fizzBuzz(int n) {
        if (n == 0) return;
        if (n % 3 == 0) System.out.print("Fizz");
        if (n % 5 == 0) System.out.print("Buzz");
        if ((n % 3) * (n % 5) != 0) System.out.print(n);
        System.out.println();
        fizzBuzz(n-1);
    }

    public static void main(String[] args) {
        fizzBuzz(100);
    }
}
