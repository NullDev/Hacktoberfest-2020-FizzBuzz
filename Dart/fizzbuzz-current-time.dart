//Check if the time at the instant is Fizz Buzz FizzBuzz or Lazy
//Author: @gautambagla


import 'dart:core';
import 'dart:async';

enum me{Fizz,Buzz,Lazy}

void main() {
  Timer.periodic(Duration(seconds: 1), (timer){
    var date = DateTime.now();
    print(whatAmI(date.millisecond) == 'Lazy' ? (date.hour.toString() + ':' + date.minute.toString() + ':' + date.second.toString() + ':' + date.millisecond.toString()) : whatAmI(date.millisecond));
    if(timer.tick == 10)
      timer.cancel();
  });
}

whatAmI(int check_me){
  String youAre = '';
  if (iAmFizz(check_me))
    youAre += promotedTo(me.Fizz);
  if (iAmBuzz(check_me))
    youAre += promotedTo(me.Buzz);
  if (iAmLazy(check_me))
    youAre += promotedTo(me.Lazy) ;
  return youAre;
}

promotedTo(me promotion){
  if (promotion == me.Fizz)
    return 'Fizz';
  if (promotion == me.Buzz)
    return 'Buzz';
  return 'Lazy';
}

iAmFizz(int fizz){
  if (fizz % 3 == 0)
    return true;
  return false;
}

iAmBuzz(int buzz){
  if (buzz % 5==0)
    return true;
  return false;
}

iAmLazy(int lazy){
  if (lazy % 3 != 0 && lazy % 5 != 0)
    return true;
  return false;
}