// FizzBuzz solution using go-routines in golang 
// Author: @hackbansu
package main

import "fmt"
import "sync"

// Create wait group so that we can wait for the go routines to finish
var wg sync.WaitGroup

func main() {
    for i := 1; i <= 100; i++ {
		// add to the wait group
		wg.Add(1)

		// call the go routine
		go FizzBuzzRoutine(i)

		// wait for the go routine to finish as we want sequential output
		wg.Wait()
	}
}

func FizzBuzzRoutine(value int) {
	defer wg.Done()
	if value % 3 == 0 {
		fmt.Print("Fizz")
	} 
	if value % 5 == 0 {
		fmt.Print("Buzz")
	}
	
	if (value % 3 != 0 && value % 5 != 0){
		fmt.Print(value)
	}

	fmt.Println("")
}
