// [Elegant oneliner using array-map with 77 charaters]
// Author: @madarsbiss

fizzbuzz=n=>[...Array(n)].map((e,i)=>`${++i%3?"":"Fizz"}${i%5?"":"Buzz"}`||i)
