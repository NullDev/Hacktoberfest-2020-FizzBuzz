bool res(i, j){
  return i%j==0;
}
void main() {
  for(int i=1;i<=100;i++){
    bool Fizz= res(i, 3);
    bool Buzz= res(i, 5);
    switch(Fizz&Buzz){
      case true:{
        print("FizzBuzz");
        break;
      }
      case false:{
        if(Fizz)
          print("Fizz");
        else if(Buzz)
          print("Buzz");
        else
          print(i);
      }
    }
  }
}
