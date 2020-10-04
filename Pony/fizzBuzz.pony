//FizzBuzz using Pony programming language
//Autor: Gareffmz

use "collections"

actor Main

  new create(env: Env) =>

// "Range" is the way to specify the loop range (1 to 100 in this case)
// I32 is a primitive data type like integer, there are others like I64 for floats, etc...

    for i in Range[I32](1, 100) do 
      if (i % 15) == 0 then
         env.out.print("FizzBuzz")
      elseif (i % 5) == 0 then
         env.out.print("Buzz")
      elseif (i % 3) == 0 then
        env.out.print("Fizz")
      else
      env.out.print(i.string())
      end
    end