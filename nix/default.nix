# Vanilla implementation in nix (The language for the package manager nix)
# Author: @CRTified

{pkgs ? (import <nixos> {})}:

with pkgs.lib;
let
  # Check for divisibility by 3 by:
  # - Checking against a list if n is single-digit
  # - Calculating the sum of digits otherwise, checking its divisibility by 3
  divisibleBy3 = n:
    if (stringLength "${toString n}") > 1 then
      divisibleBy3 (foldr
        (v: acc: (toInt v) + acc)
        0
        (stringToCharacters (toString n))
      )
    else
      elem n [0 3 6 9];

  # Check  for divisibility by 5 by:
  # Checking if the last digit is 0 or 5
  divisibleBy5 = n:
    let
      lastChar = last (stringToCharacters (toString n));
    in
      elem lastChar [ "0" "5" ];

  # Build FizzBuzz String
  fizzbuzz = v:
    let
      isDiv3 = divisibleBy3 v;
      isDiv5 = divisibleBy5 v;
    in
      if isDiv3 && isDiv5 then
        "FizzBuzz"
      else if isDiv5 then
        "Buzz"
      else if isDiv3 then
        "Fizz"
      else
        toString v;
in
pkgs.writeText
  "fizzbuzz.txt"
  (concatStringsSep
    "\n"
    (map fizzbuzz (range 1 100)) # Apply on all numbers between 1 and 100
  )
