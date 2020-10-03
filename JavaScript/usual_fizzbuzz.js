// Author: @alexandrunst

for (var i = 0; i < 100; i++) {
  if (i % 3 == 0 && i % 5 == 0) {
    console.log("fizzbuzz");
    continue;
  } else if (i % 3 == 0) {
    console.log("fizz");
    continue;
  } else if (i % 5 == 0) {
    console.log("buzz");
    continue;
  } else {
    console.log(i);
  }
}
