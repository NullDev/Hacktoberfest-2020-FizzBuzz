(*  FizzBuzz in OCaml
    Author: @vimarsh6739    
*)

let value i = 
  if i mod 15 == 0 then "FizzBuzz"
  else if i mod 3 == 0 then "Fizz"
  else if i mod 5 == 0 then "Buzz"
  else string_of_int(i)
;;

let rec loop i n=
  if i<=n then 
    let () = print_endline (value i) in loop (i+1) n
;;

loop 1 100