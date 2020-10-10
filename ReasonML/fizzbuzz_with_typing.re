// FizzBuzz - now with TYPES!
// Depends on Belt
// Author: Artemiy Solopov

module FizzBuzz {
  type t = 
    | None
    | Fizz(t)
    | Buzz(t)
    | Just(int);

  let make = (a: int): t => {
    let q = ref(None)
      if (a mod 5 == 0) { q := Buzz(q^) }
    if (a mod 3 == 0) { q := Fizz(q^) }
    if (q^ == None) { q := Just(a) }
    q^
  };

  let rec _toStr = (n: t) => {
    switch(n) {
      | None => "";
      | Fizz(nn) => "Fizz" ++ _toStr(nn)
      | Buzz(nn) => "Buzz" ++ _toStr(nn)
      | Just(num) => string_of_int(num)
      }
  };

  let fizzbuzz = (n: int) => n -> make -> _toStr;
}

Belt.Range.forEach(1, 100, n => {
  n -> FizzBuzz.fizzbuzz -> print_endline;
})
