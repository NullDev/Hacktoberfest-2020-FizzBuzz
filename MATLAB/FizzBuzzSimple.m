% Simple MATLAB FizzBuzz
% Author: @veotani
for number = 1:101
    if  mod(number, 15) == 0
        fprintf('FizzBuzz')
    elseif  mod(number, 3) == 0
        fprintf('Fizz')
    elseif mod(number, 5) == 0
        fprintf('Buzz')
    else 
        fprintf(number)
    end
end
