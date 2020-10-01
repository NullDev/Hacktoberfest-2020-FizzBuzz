import java.util.Scanner;
import java.util.stream.IntStream;
 
public class Main {
 
	public static void main(String[] args) {
 
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number:");
		int n = s.nextInt();
		IntStream.rangeClosed(1, n)
	    .mapToObj(i -> i % 3 == 0 ? (i % 5 == 0 ? "FizzBuzz " : "Fizz ") : (i % 5 == 0 ? "Buzz " : i+" "))
	    .forEach(System.out::print);
		s.close();
	}
}
 
