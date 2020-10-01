-- author: @GauravPoosarla 

with recursive numbers (i) as (
   select *
   from (values (1)) as t
   union all
   
   select n.i + 1
   from numbers n
   where n.i < 100
)
select i,
       case 
          when mod(i, 15) = 0 then 'Fizz Buzz'
          when mod(i,  5) = 0 then 'Buzz'
          when mod(i,  3) = 0 then 'Fizz'
          else cast(i as varchar)
       end as fz
from numbers 
order by i;
