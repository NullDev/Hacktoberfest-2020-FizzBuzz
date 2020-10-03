// FizzBuzz with while loop and printing strings of fizz,buzz and fizzbuzz
// Author: @acaa06

void main() {
  var fizz='fizz',buzz='buzz',fizzbuzz='fizzbuzz';
  int i=1;
  while(i<=100) {
    
      if((i % 3 == 0) && (i % 5 == 0)){
      
      print(fizzbuzz);
      }
     else {
       if ((i % 3 == 0) || (i % 5 == 0)) {
      if (i % 3 == 0) {
        print(fizz);
      }
      if (i % 5 == 0) {
        print(buzz);
      }
    }
    else{
print(i);
    }}
    i++;
  }
}
