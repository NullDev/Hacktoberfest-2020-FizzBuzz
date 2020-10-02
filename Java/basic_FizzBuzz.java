public class Solution{
    public static void main(String[]args){
        for(int i = 1; i<=100; i++){
            if(i % 3 == 0)System.out.print("Fizz");
            if(i%5==0)System.out.print("Buzz");
            else if(i%3 != 0)
            System.out.print(i);
            System.out.println();
        }
    }
}
