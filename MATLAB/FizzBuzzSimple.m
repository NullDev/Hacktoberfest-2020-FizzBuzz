% Simple MATLAB FizzBuzz
% Author: @veotani
for number = 1:101
    if  mod(number, 15) == 0
        disp('FizzBuzz')
    elseif  mod(number, 3) == 0
        disp('Fizz')
    elseif mod(number, 5) == 0
        disp('Buzz')
    else 
        disp(number)
    end
end