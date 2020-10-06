// A recursive implementation of FizzBuzz in Go
// Author: @evamy

package main

import (
	"fmt"
	"strconv"
)

func main() {
	PrintFizzBuzz(100)
}

func PrintFizzBuzz(n int) {
	fizzbuzz(1, n)
}

func fizzbuzz(current int, n int) {
	if (current%3 == 0 && current%5 == 0) {
		fmt.Println("FizzBuzz")
	} else if current%3 == 0 {
		fmt.Println("Fizz")
	} else if current%5 == 0 {
		fmt.Println("Buzz")
	} else {
		fmt.Println(strconv.Itoa(current))
	}

	if current < n {
		fizzbuzz(current+1, n)
	}

	return
}