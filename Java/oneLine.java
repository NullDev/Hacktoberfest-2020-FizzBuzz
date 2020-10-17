//One line solution
// author: @brigadierpratap
import java.util.*;
class FizzBuzz{
     public static void main(String args[]){
        for(int i=1;i<101;i++){
            System.out.println((i%3==0 && i%5==0)?"FizzBuzz":(i%3==0?"Fizz":(i%5==0?"Buzz":i))+"\n");
        }
    }
    
}
