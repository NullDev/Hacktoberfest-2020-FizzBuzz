// FizzBuzz Go Concurrency
// Author: @ntsd

package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

func fizzBuzz(i int, outChan chan<- string, wg *sync.WaitGroup) {
	time.Sleep(time.Duration(i) * time.Millisecond)
	if i%15 == 0 {
		outChan <- "FizzBuzz"
	} else if i%3 == 0 {
		outChan <- "Fizz"
	} else if i%5 == 0 {
		outChan <- "Buzz"
	} else {
		outChan <- strconv.Itoa(i)
	}
	wg.Done()
}

func main() {
	n := 100
	outChan := make(chan string)
	wg := new(sync.WaitGroup)
	go func() {
		wg.Add(n)
		for i := 1; i <= n; i++ {
			go fizzBuzz(i, outChan, wg)
		}
		wg.Wait()
		close(outChan)
	}()
	for output := range outChan {
		fmt.Println(output)
	}
}
