// FizzBuzz using Java Streams in one line 
// Author: @sudesh1611 

import java.util.stream.IntStream;

public class FizzBuzz_StreamOneLiner {

    public static void main(String[] args) {
        IntStream.range(1, 101).mapToObj(i -> (i % 15 == 0 ? "FizzBuzz" : (i % 3 == 0 ? "Fizz" : (i % 5 == 0 ? "Buzz" : String.valueOf(i))))).forEach(i -> System.out.println(i));
    }
}
