
/******************************************************************************

                            This code is developed by Sombit Bose 
                        This program uses sliding window and modulo
                    opoerator for classifying fizz, buzz and fizz_buzz.

*******************************************************************************/

import java.util.HashSet;
import java.util.Set;

public class FizzBuzz_SlidingWindow {
	public static void main(String[] args) {
		int start_3 = 1, start_5 = 1, end_3 = 3, end_5 = 5;
		Set<Integer> fizz = new HashSet<Integer>();
		Set<Integer> buzz = new HashSet<Integer>();
		Set<Integer> fizz_buzz = new HashSet<Integer>();
		while (end_3 < 100 && end_5 < 100) {
			if (end_3 == end_5)
				fizz_buzz.add(end_3);
			else {
				fizz.add(end_3);
				if (end_5 % 15 != 0)
					buzz.add(end_5);
			}
			end_3 += 3;
			start_3 += 3;
			if (end_3 > end_5) {
				end_5 += 5;
				start_5 += 5;
			}
		}
		System.out.println("The list of fizz numbers\n" + fizz);
		System.out.println("The list of buzz numbers\n" + buzz);
		System.out.println("The list of fizz buzz numbers\n" + fizz_buzz);
	}
}
