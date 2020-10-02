// FizzBuzz without using 'F', 'i', 'z', 'B', or 'u'
// Hexadecimal code points to reference the letters 
// Loop using .map over an empty array spread into an array
// Author: @jacobshu

j='\x46\x69\x7a\x7a';
k='\x42\x75\x7a\x7a';
[...Array(100)].map((_,m)=>console.log((++m%3?'':j)+(m%5?'':k)||m))