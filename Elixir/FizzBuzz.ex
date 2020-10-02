defmodule FizzBuzz do
  def fizz do
    (1..100)
    |> Enum.map(&buzz/1)
    |> Enum.each(&IO.puts/1)
  end

  defp buzz(i) when rem(i, 15) == 0, do: "FizzBuzz"
  defp buzz(i) when rem(i, 5)  == 0, do: "Buzz"
  defp buzz(i) when rem(i, 3)  == 0, do: "Fizz"
  defp buzz(i),                      do: Integer.to_string(i)
end