// Solution of FizzBuzz in golang 
// author: @divyanshugit
package main
import "fmt"
func main() {
    for i := 1; i <= 100; i++ {

        if i%3 == 0 {
            // Multiple of 3
            fmt.Printf("fizz")
        }
        if i%5 == 0 {
            // Multiple of 5
            fmt.Printf("buzz")
        }

        if i%3 != 0 && i%5 != 0 {
            // Neither, so print the number itself
            fmt.Printf("%d", i)
        }

        // A trailing new line (so both fizz + buzz can be printed on the same line)
        fmt.Printf("\n")

    }
}
