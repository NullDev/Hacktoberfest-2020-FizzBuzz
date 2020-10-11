fizzbuzz <- function(num) {
   if (num %% 3  == 0 && num %% 5 == 0) {print("FizzBuzz")}
   else if (num %% 3 == 0) {print("Buzz")}
   else if (num %% 5 == 0) {print("Fizz")}
   else print(num)
}
sapply(1:100, fizzbuzz)
