module Fizzbuzz
  extend self

  def calculate_fizzbuzz_of(number : Number)
    divisible_by_3 = number.divisible_by?(3)
    divisible_by_5 = number.divisible_by?(5)

    case
    when (divisible_by_3 && divisible_by_5) then "FizzBuzz"
    when (divisible_by_3) then "Fizz"
    when (divisible_by_5) then "Buzz"
    else number
    end
  end

end