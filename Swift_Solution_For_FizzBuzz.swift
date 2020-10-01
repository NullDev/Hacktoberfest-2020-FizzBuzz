 // A FizzBuzz Solution in Swift
 // Author: @nandanhere

 // Here is a Fizbuzz program in swift! a very simple to understand language, similar to python , but very user friendly!
 
 import Foundation
 // this is the normal route someone would go through to execute fizbuzz in swift. first start a for loop
 for n in 1 ... 100{
    var str   = ""  // Initialising a string which is empty
     
     if n % 3 == 0
    {
        str += "Fizz"
        
    }
     
     if n % 5 == 0
    {
        str += "Buzz"
    }
    
    str.isEmpty ? print(n) : print(str) // We have ternary operators too!
 }
 
 /// The resulting solution gives us 100 lines, where the nth line is fizzbuzz if it is divisible by both 5 and 3, fizz if 3 and buzz if 5, or just the number if nothing.
