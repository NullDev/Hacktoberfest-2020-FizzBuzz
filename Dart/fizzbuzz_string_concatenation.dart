// FizzBuzz with string concatenation
// Author: @rmRizki

void main() {
  var output = '';
  
  for (int i = 1; i <= 100; i++) {
    if ((i % 3 == 0) || (i % 5 == 0)) {
      if (i % 3 == 0) {
        output += "Fizz" ;
      }
      if (i % 5 == 0) {
        output += "Buzz";
      }
    } else {
      output += i.toString();
    }
    output += '\n';
  }
  
  print(output);
}
