for i = 1:101
	fizzbuzz = '';
    if mod(i,3) == 0
    fizzbuzz = [fizzbuzz 'Fizz'];
	end
    if mod(i,5) == 0
    fizzbuzz = [fizzbuzz 'Buzz'];
	end
    if isempty(fizzbuzz)
	disp(i)
    else 
	disp(i)
    end
end