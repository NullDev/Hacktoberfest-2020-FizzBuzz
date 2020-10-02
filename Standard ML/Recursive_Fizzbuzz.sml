fun printfizz_buzz(n) =
	if n <= 0 then ""
	else if n mod 3 = 0 andalso n mod 5 = 0 then "fizzbuzz" ^ printfizz_buzz(n-1)
	else if n mod 3 = 0 then "fizz" ^ printfizz_buzz(n-1)
	else if n mod 5 = 0 then "buzz" ^ printfizz_buzz(n-1)
	else Int.toString(n) ^ printfizz_buzz(n-1);
