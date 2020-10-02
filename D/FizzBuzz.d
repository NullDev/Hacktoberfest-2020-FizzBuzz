/*
    FizzBuzz in D
*/
import std.stdio; 

void main(string[] args) {  
    int n = 1;
    while(n <= 100) {
        (n%3 == 0 && n%5 == 0) ? writefln("FizzBuzz") : ((n%3 == 0) ? writefln("Fizz") : ((n%5 ==0) ? writefln("Buzz") : writefln("%d", n))); 
      n++; 
   }
}