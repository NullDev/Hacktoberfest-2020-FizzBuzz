# Author: @jotagarciaz

for i in 0..100 do
   fizzbuzzstring = ""
   if i % 3 == 0
      fizzbuzzstring += "fizz"
   end
   if i % 5 == 0
      fizzbuzzstring +=  "buzz"
   end
   if fizzbuzzstring.eql? ""
      fizzbuzzstring = "#{i}"
   end
   puts fizzbuzzstring
end
