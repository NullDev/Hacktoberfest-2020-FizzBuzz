// A simple Recursive kotlin program for fizzbuzz
// Author: @JossJoestar

import java.util.Scanner

fun main(args:Array<String>){ 
    print("Give me a number please: ")
    val read = Scanner(System.`in`)  
    var number = read.nextInt()  
    fizz(1,number)
}

fun fizz(n:Int, end:Int){
    if(n%3 == 0 && n%5 ==0)
        println("FizzBuzz")
    else if(n%5==0)
        println("Buzz")
    else if(n%3==0)
        println("Fizz")
    else
        println("") 
    if(n < end)
        return fizz(n+1, end)
}