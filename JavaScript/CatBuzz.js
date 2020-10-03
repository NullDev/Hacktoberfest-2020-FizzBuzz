//CatBuzz(0,100)

CatBuzz(indexFrom , indexTo){
    for(var i = indexFrom; i<=indexTo ; i++ ){
      if( i % 3===0 && i % 5===0 ){
        console.log(i+" = FizzBuzz");
      } else if( i % 3 === 0 ){
        console.log(i+" = Fizz");
      }else if(i % 5 === 0 ){
        console.log(i+" = Buzz");
      } else {
        console.log(i);
      }
    }
}