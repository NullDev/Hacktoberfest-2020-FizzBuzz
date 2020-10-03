# This solution explore better the elixir way using case to match values
# and tuples to be easier to read
# Author: @uduDudu

defmodule FizzbuzzTuple do
  def fizzBuzz(n) do
    case {rem(n, 3) == 0, rem(n, 5) == 0} do
      {false, false} -> n
      {true, false} -> "Fizz"
      {false, true} -> "Buzz"
      {true, true} -> "FizzBuzz"
    end
  end
end
