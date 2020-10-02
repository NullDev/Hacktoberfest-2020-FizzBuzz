# Simple MYSql PROCEDURE implementation for FizzBuzz
# Author: @SGopinath89
delimiter //
	create procedure FizzBuzz()
	begin
		declare x int default 1;
		declare msg1 varchar(8) default '';
		declare msg2 text default '';
		
		WHILE x <= 100 do
			IF x%15 = 0 then
				set msg1 = 'FizzBuzz';
			ELSEIF x%3 = 0 then
				set msg1 = 'Fizz';
			ELSEIF x%5 = 0 then
				set msg1 = 'Buzz';
			ELSE
				SET msg1 = x;
			END IF;	
			set msg2 = concat(msg2,msg1,' ');
			set x = x+1;
		END WHILE;
		
		select msg2;
	end //
delimiter ;

call FizzBuzz();