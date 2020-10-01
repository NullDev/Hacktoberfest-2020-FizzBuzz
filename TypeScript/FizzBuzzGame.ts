class fizzbuzzGame{
    fizzbuzzNumber:number=0
    fizzbuzz(){
        // a forloop which run for the number from 1 to 100
        for(this.fizzbuzzNumber=1;this.fizzbuzzNumber<100;this.fizzbuzzNumber++){
          if(this.fizzbuzzNumber%3==0 ){
              //if the number is divided by 3 then it prints "Fizz"
            console.log("fizz")
          }else if(this.fizzbuzzNumber%5==0){
              //if the number is divided by 3 then it prints "buzz"
            console.log("Buzz")
          }else if(this.fizzbuzzNumber%3==0 && this.fizzbuzzNumber%5==0){
              //if the number is divided by 3 and also 5 then it prints "buzz"
            console.log("FizzBuzz")
          }
          else{
              //else it will print the only number
            console.log(this.fizzbuzzNumber)
          } 
        }
      }
}
