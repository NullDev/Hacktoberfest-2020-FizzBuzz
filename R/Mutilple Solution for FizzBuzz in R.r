# Multiple solution for Fizzbuzz in R 
# Author - pranavanand24 

# 1) A Better Solution Using a For Loop

fbnums <- 1:50
output <- vector()

for (i in fbnums) {
  output[i] <- ""
  
  if (i %% 3 == 0) {output[i] <- paste0(output[i], "Fizz")}
  if (i %% 5 == 0) {output[i] <- paste0(output[i], "Buzz")}
  if (output[i] == "") {output[i] <- i}
}

print(output)

# 2) A Functional Solution Using map()

library(tidyverse)

fbnums <- 1:50

fbmap <- function(input, mod1, mod2, exp1, exp2) {
  output <- ""
  
  if (input %% mod1 == 0) {output <- paste0(output, exp1)}
  if (input %% mod2 == 0) {output <- paste0(output, exp2)}
  if (output == "") {output <- as.character(input)}
  
  return(output)
}

output <- map_chr(fbnums, ~ fbmap(.x, 3, 5, "Fizz", "Buzz"))
print(output)

# 3) A Package Solution Using FizzBuzzR

install.packages("fizzbuzzR")

library(fizzbuzzR)

fizzbuzz(start = 1, end = 50, step = 1, mod1 = 3, mod2 = 5)