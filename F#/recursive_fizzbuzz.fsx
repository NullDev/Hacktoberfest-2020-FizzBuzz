// A recursive fizzbuzz solution implemented in F#. Constructs a linked list of strings recursively before iterating over them to print them out.
// Author: @rosalogia
let divisibleBy x y = y % x = 0

let fbmap = function
    | x when x |> divisibleBy 3 && x |> divisibleBy 5 -> "fizzbuzz"
    | x when x |> divisibleBy 3 -> "fizz"
    | x when x |> divisibleBy 5 -> "buzz"
    | x -> string x


let rec fizzbuzz n = if n <= 100 then fbmap n :: fizzbuzz (n + 1) else []

fizzbuzz 1
|> List.iter (printfn "%s")
