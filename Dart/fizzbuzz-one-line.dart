// One line solution in Dart language. If you open it, it will beautify the code, so will become not-one-line code.
// Author: @iam-agf

void main() {List<int>.generate(100, (int index) => index).forEach((index) {if (index % 3 == 0) {print("Fizz");} else if (index % 5 == 0) {print("Buzz");} else print(index);});}
