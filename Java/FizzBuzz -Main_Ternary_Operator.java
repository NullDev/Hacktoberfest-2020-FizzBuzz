/*
 FizzBuzz Using For-Loop and Ternary Operator. Applied all the logic of Fizz and Buzz in single line only.
 Author: @akashprasher
*/

public class Main {
	public static void main(String[] args) {
	    for(int i = 1; i <= 100; i++) System.out.println((i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : (i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i));
	}
}
