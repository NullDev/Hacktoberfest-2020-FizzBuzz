// FizzBuzz using conditional and loop inside list 😎
// Author: @rmRizki

void main() {
  List<String> output = [
    for (int i = 1; i <= 100; i++) 
       (i % 15 == 0) ? "FizzBuzz" :
       (i % 3 == 0) ? "Fizz" :
       (i % 5 == 0) ? "Buzz" :
       '$i'
  ];
  
  for(var i in output){
    print(i);
  }
}
