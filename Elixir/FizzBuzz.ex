defmodule FizzBuzz do
	def perform_count(total_count) when total_count >= 0 do
		total_count
		|> count()
		|> Enum.reverse()
		|> print()
	end
	
	defp count(0) do
		[]
	end
	
	defp count(count) when rem(count, 3) == 0 and rem(count, 5) == 0 do
		["fizzbuzz" | count(count - 1)]
	end
	
	defp count(count) when rem(count, 3) == 0 do
		["fizz" | count(count - 1)]
	end
	
	defp count(count) when rem(count, 5) == 0 do
		["buzz" | count(count - 1)]
	end
	
	defp count(count) do
		[Integer.to_string(count) | count(count - 1)]
	end

	defp print([]) do
	end
	
	defp print([head | tail]) do
		IO.puts(head)
		
		print(tail)
	end	
end