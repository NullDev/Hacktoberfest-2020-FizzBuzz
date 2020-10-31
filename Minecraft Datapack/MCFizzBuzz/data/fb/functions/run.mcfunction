#A recursive FizzBuzz MCFunction caller to be run in minecraft
#Author: cakoshakib

# Basically initializes a ton of variables bc minecraft does not allow operations with numbers normally
scoreboard objectives add FizzBuzz dummy 
# Primary carrier variable that will be incremented
scoreboard players set carrier FizzBuzz 1 
scoreboard objectives add mod dummy 
scoreboard players set three mod 3 
scoreboard players set five mod 5 
scoreboard players set zero mod 0 
scoreboard players set hundred mod 100 
scoreboard players set one mod 1 
function fb:recursive 