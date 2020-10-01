//Fizzbuzz program in dart
//author yasharth291
import 'dart:io';
void main() {
  int i = 1;
  while (i <= 100) {
    if ((i % 3 == 0) || (i % 5 == 0)) {
      if (i % 3 == 0) {
        stdout.write("Fizz");
      }
      if (i % 5 == 0) {
        print("Buzz");
      } else {
        print("");
      }
    } else {
      print(i);
    }
    i++;
  }
}
