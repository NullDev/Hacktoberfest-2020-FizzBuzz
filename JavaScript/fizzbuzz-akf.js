// FizzBuzz JavaScript solution (Readable, Extendable)
// Author: @akojif

FizzBuzz = function() {
  var length = 100,
      result = new Array(length);

  for (i=0; i < length; i++) {
    var seqNum     = i + 1,
        div3       = ((seqNum % 3) === 0),
        div5       = ((seqNum % 5) === 0),

        isFizzy    = div3,
        isBuzzy    = !div3 && div5,
        isFizBuzzy = div3 && div5,

        word;

    if (isFizzy)    { word = "Fizz" };
    if (isBuzzy)    { word = "Buzz" };
    if (isFizBuzzy) { word = "FizzBuzz" };

    result[i] = word || seqNum;
    word = null;
  }

  return result;
}

FizzBuzz().forEach( function(elm) { console.log(elm) })
