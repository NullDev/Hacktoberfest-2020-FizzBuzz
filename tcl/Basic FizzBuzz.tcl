#Basic Program for FizzBuzz in tcl language
#Author: @BreathlessVictor


for { set a 1}  {$a < 101} {incr a} {
   if { $a % 15 == 0 }    {
       puts "FizzBuzz"
   }    elseif { $a % 3 == 0 }   {
      puts "Fizz"
   }   elseif { $a % 5 == 0 }    {
      puts "Buzz"
   }    else    {
      puts "$a"
   }
}
