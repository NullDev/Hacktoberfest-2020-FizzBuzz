class Solution {
//function to print fizz for multiples of 3 and buzz in multiples of 5 and fizzbuzz for multiples of both 3 and 5
    public List<String> fizzBuzz(int n) {
      List<String> lt = new ArrayList<>();
        String str="";
        for(int i=1;i<=n;i++){
           if(i%3==0 && i%5!=0){
               lt.add("Fizz");
           }
             if(i%5==0 && i%3!=0){
                 lt.add("Buzz");
            }
            if (i%3==0 && i%5==0 && i!=1){
                 lt.add("FizzBuzz");
            }
            if(i%3!=0 && i%5!=0){
                 lt.add(Integer.toString(i));
            }
            
        }
        return lt;
    }
}
