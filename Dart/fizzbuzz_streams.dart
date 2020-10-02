// FizzBuzz using dart streams
// Author: @rmRizki

void main() async {
  var output = '';
  var i = countStream(100);
  i.forEach((i)  {
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
    print(output);
  });
}

Stream<int> countStream(int to) async* {
  for (int i = 1; i <= to; i++) {
    yield i;
  }
}
