(*
    Basic FizzBuzz implementation in Wolfram Language

    With wolframscript installed, run with:
        wolframscript -file FizzBuzz.wls

    Author: @PAndaContron
*)

Do[
    Print[
        If[Divisible[i, 15], "FizzBuzz",
            If[Divisible[i, 3], "Fizz",
                If[Divisible[i, 5], "Buzz", i]
            ]
        ]
    ],
    {i, 100}
]
