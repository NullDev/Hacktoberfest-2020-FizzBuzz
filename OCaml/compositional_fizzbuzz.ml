(* A FizzBuzz implementation in OCaml that
 * avoids imperative patterns such as
 * if/else and loops, instead opting
 * for pattern matching and function
 * composition.
 *
 * author: @rosalogia
 * *)

open Batteries

let () =
    (1--100) (* This operator is defined in Batteries and returns an Enum *)
    |> Enum.map (function
                    | x when x mod 3 = 0 && x mod 5 = 0 -> "FizzBuzz"
                    | x when x mod 3 = 0                -> "Fizz"
                    | x when x mod 5 = 0                -> "Buzz"
                    | x                                 -> Printf.sprintf "%i" x)
    |> List.of_enum
    |> String.concat "\n"
    |> print_string
