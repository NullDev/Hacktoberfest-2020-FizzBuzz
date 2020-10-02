for x=1,100 do  
    local divBy3, divBy5 = x % 3 == 0, x % 5 == 0 
     
    if divBy3 and divBy5 then 
      print("FizzBuzz") 
    elseif divBy3 then 
      print("Fizz") 
    elseif divBy5 then 
      print("Buzz") 
    else 
      print(x)  
    end 
end
