//static methods to check whether Fizz or Buzz or Both or None, no need to instantiate
// @utkarsh48

class FizzBuzz{
  static isFizz(value){
    if(value%3===0){
      return true;
    }
    else return false;
  }
  static isBuzz(value){
    if(value%5===0){
      return true;
    }
    else return false;
  }
  static isFizzBuzz(value){
    if(value%15===0){
      return true;
    }
    else return false;
  }
  static notFizzOrBuzz(value){
    if(value%3===0 || value%5===0){
      return false;
    }
    else return true;
  }
};
