// An implementation of FizzBuzz in Go which checks 3 and 5 multiple using math tricks
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

	for current < n {
		var flag = false

		if checkThree(current) {
			fmt.Print("Fizz")
			flag = true
		}
		if checkFive(current) {
			fmt.Print("Buzz")
			flag = true
		}

		if flag == false {
			fmt.Println(strconv.Itoa(current))
		} else {
			fmt.Println()
		}

		current++
	}
}

func checkThree(current int) bool{
	var sum int = sumDigits(current)

	if (sum == 3 || sum == 6 || sum == 9) {
		return true
	}

	return false
}

func sumDigits(current int) int{

	if (current < 10) {
		return current
	}
	var sum int = 0
	for (current > 0) {
		sum += current % 10
		current = current / 10
	}

	return sumDigits(sum)
}

func checkFive(current int) bool {
	if (current%10 == 0 || current%10 == 5) {
		return true
	}

	return false
}