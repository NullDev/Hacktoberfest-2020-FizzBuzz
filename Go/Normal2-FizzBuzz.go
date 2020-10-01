// A simple#2 implementation of FizzBuzz in Go
// Author: @n0nz
// https://play.golang.org/p/CUKIi6ZBf6H

package main

import (
	"fmt"
	"strconv"
)

func main() {
	PrintFizzBuzz(100)
}

func PrintFizzBuzz(n int) {
	for i := 0; i <= n; i++ {
		fmt.Println(fizzbuzz(i))
	}
}

func fizzbuzz(n int) string {
	var rtn string
	if n%3 == 0 {
		rtn += "fizz"
	}

	if n%5 == 0 {
		rtn += "buzz"
	}

	if rtn == "" {
		return strconv.Itoa(n)
	}

	return rtn
}
