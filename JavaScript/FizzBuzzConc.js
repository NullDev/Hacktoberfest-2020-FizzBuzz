//author GouthamSuredran
// KeyValue and concat()

const words = {3:"Fizz", 5:"Buzz"};

const fizzBuzz = (i) => {
  if (i%15 ==0)
  return words[3].concat(words[5]);
  else if(i%3 ==0)
  return words[3];
  else if (i%5 == 0) 
  return words[5];
  else return i;
}

for(i=1;i<=100;i++) {
  console.log(fizzBuzz(i));
}


