//Fizzbuzz using Lengths of Lists.
// username @rahulchuchra

void main() {
  List<bool> div3 = []; //for numbers divisible by 3
  List<bool> div5 = []; //for numbers divisible by 5
  List<bool> notDiv = []; //for numbers not divisible by either

  for (int x = 1; x <= 100; x++) {
    x % 3 == 0
        ? div3.add(true)
        : notDiv.add(true); //adds true to the lists depending upon conditions
    x % 5 == 0 ? div5.add(true) : notDiv.add(true);
    check(div3, div5, notDiv, x); //function called
    div3.clear();
    div5.clear();
    notDiv.clear();
  }
}

void check(List a, List b, List c, int i) {
  if (a.length == b.length && a.length > c.length) {
    print('FizzBuzz');
  } else if (a.length > b.length) {
    print(
        'Fizz'); //compares lengths of lists and prints out "fizz","buzz" or "fizzbuzz"
  } else if (b.length > a.length) {
    print('Buzz');
  } else {
    print(i);
  }
}
