var i = 0;

function increment() {
  i++;
  if(i % 3 === 0 && i % 5 === 0) {
      console.log('fizzbuzz');
  } else if(i % 3 === 0) {
      console.log('fizz');
  } else if(i % 5 === 0) {
      console.log('buzz');
  } else {
      console.log(i);
  }
}

let timer = setTimeout(function myTimer() {
  increment();
  timer = setTimeout(myTimer, 1000);
}, 1000);

setTimeout(() => {
  clearTimeout(timer);
}, 100000);