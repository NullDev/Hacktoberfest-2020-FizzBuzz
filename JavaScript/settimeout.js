(() => {
  for (let i = 100; i > 0; i--) {
    setTimeout(() => {
      let isFizzBuss = false;
      let output = '';
      if (i % 3 == 0) {
        output += 'Fizz';
        isFizzBuss = true;
      }
      if (i % 5 == 0) {
        output += 'Buzz';
        isFizzBuss = true;
      }
      if (!isFizzBuss) output += i;
      console.log(output);
    }, i);
  }
})();
