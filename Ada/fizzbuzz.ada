with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
procedure Hello is
    Div_By_3 : Boolean := false;
    Div_By_5 : Boolean := false;
begin
For_Loop :
   for I in Integer range 1 .. 100 loop
  
      Div_By_3 := I mod 3 = 0;
      Div_By_5 := I mod 5 = 0;
      
    if Div_By_3 and Div_By_5 then 
        Put_Line("FizzBuzz");
    elsif Div_By_3 then
        Put_Line("Fizz");
    elsif Div_By_5 then
        Put_Line("Buzz");
    else
        Put( I );
        New_Line(1);
    end if;
      
   end loop For_Loop;

end Hello;