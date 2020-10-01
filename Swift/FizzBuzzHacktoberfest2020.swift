//
//  FizzBuzzHacktoberfest2020.swift
//
//  Created by Jesse Ruiz on 10/1/20.
//
// I decided to solve this using a repeat while loop
// because I haven't seen a solution like this.
//
// GitHub: @jesseleeruiz

import Foundation

func fizzBuzz() {
    var count = 0
    
    repeat {
        for number in 1 ... 100 {
            if number % 3 == 0 && number % 5 == 0 {
                print("FizzBuzz")
            } else if number % 3 == 0 {
                print("Fizz")
            } else if number % 5 == 0 {
                print("Buzz")
            } else {
                print(number)
            }
            count += 1
        }
    } while count != 100
}
