//fizzbuzz java programming
// Author: @Chamudi

public class Solution{
  /**
  NOTE: This has redundancy as (i%3==0) is repeated twice. TO improve it, there are better Solutions
  */
  public static void main(String[]args){
    for(int i = 1; i<=100; i++){
      if(i%3==0)//if i is divisble by 3
        System.out.print("Fizz");
      if(i%5==0)//if i is divisble by 5
        System.out.print("Buzz");
      else if(i%3 != 0)//if not divisble by 3 or 5
        System.out.print(i);
      System.out.println();
    }
  }
}
