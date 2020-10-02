for n=1:100
    if modulo(n,3)==0 & modulo(n,5)>0 then
        disp("Fizz")
    elseif modulo(n,5)==0 & modulo(n,3)>0 then
        disp("Buzz")
    elseif modulo(n,5)==0 & modulo(n,3)==0 then
        disp("FizzBuzz")
    else
        disp(string(n))
    end
end
