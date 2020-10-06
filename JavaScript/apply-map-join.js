// [Didn't see anyone using apply method, so here it is]
// Author: @madarsbiss

const fizzBuzz = () =>
  Array.apply(null, {length: 100}).map(function(val, index) {
    return (++index%3?'':'Fizz')+(index%5?'':'Buzz')||index;
  }).join('\n')
