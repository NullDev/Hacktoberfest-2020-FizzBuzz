// A simple program of FizzBuzz
// Author: @siddhant2155
import Foundation

var count_3 = 0
var count_5 = 0

for i in 0...100 {
	count_3 += 1
	count_5 += 1
	var str = ""
	if count_3 == 3 {
		str += "Fizz"
		count_3 = 0
	}
	if count_5 == 5 {
		str += "Buzz"
		count_5 = 0
	}
	print( str.isEmpty ? i : str)
}