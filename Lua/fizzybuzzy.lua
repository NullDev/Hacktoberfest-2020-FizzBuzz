counter = 100
while (counter > 0 )
do
  if counter % 15 == 0 then print(counter..' FizzBuzz') 
  elseif counter % 3 == 0 then print(counter..' Fizz') 
  elseif counter % 5 == 0 then print(counter..' Buzz') 
  end
  counter = counter - 1
end
