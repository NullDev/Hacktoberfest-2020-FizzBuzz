# Recursive FizzBuzz MCFunction
# Author: @cakoshakib

# initialize variables
scoreboard players set mod3 mod 0 
scoreboard players set mod5 mod 0
scoreboard players operation mod3 mod = carrier FizzBuzz 
# mod3 holds carrier%3
scoreboard players operation mod3 mod %= three mod 
# mod5 holds carrier%5
scoreboard players operation mod5 mod = carrier FizzBuzz
scoreboard players operation mod5 mod %= five mod 

# if chain to test if FizzBuzz
execute if score mod3 mod = zero mod unless score mod5 mod = zero mod run tellraw @a "Fizz"
execute if score mod5 mod = zero mod unless score mod3 mod = zero mod run tellraw @a "Buzz"
execute if score mod5 mod = zero mod if score mod3 mod = zero mod run tellraw @a "FizzBuzz"
execute unless score mod3 mod = zero mod unless score mod5 mod = zero mod run tellraw @a {"score":{"name":"carrier","objective":"FizzBuzz"}}

# Increment and recursive call
scoreboard players operation carrier FizzBuzz += one mod
execute if score carrier FizzBuzz <= hundred mod run function fb:recursive