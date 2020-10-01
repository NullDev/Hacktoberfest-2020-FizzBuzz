//fizzbuzz Go programming
// Author: @Chamudi
package main

import "fmt"

func main() {
        for i := 1; i < 101; i++ {
                s := fmt.Sprintf("%d", i)
                if i%3 == 0 {
                        s = "Fizz"
                        if i%5 == 0 {
                                s += "Buzz"
                        }
                } else if i%5 == 0 {
                        s = "Buzz"
                }
                fmt.Println(s)
        }
}