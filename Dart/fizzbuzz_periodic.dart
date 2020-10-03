// Periodic FizzBuzz events with Timer
// Author: @gautambagla

import 'dart:async';
import 'dart:core';

void main() {
  int count = 1;
  Timer.periodic(Duration(milliseconds: 500), (timer){
    String printer = '';
    if(count%3 == 0)
      printer += 'Fizz';
    if(count%5 == 0){
      printer += 'Buzz';
    }
    if (count%3 != 0 && count%5 != 0)
      printer += count.toString();
    print(printer);
    if (count == 100)
      timer.cancel();
    count += 1;
  });
}