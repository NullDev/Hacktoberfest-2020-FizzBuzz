num = String.to_integer(IO.gets "")

1..num
|> Enum.each(fn n -> 
    cond do
        rem(n, 3) == 0 and rem(n, 5) == 0 -> IO.puts("FizzBuzz")
        rem(n, 3) == 0 -> IO.puts("Fizz")
        rem(n, 5) == 0 -> IO.puts("Buzz")
        true -> IO.puts(n)
    end
end)
