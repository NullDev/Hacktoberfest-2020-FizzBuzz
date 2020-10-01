-- Simple Elm FizzBuzz implementation
-- Author: @veotani
import Html exposing (text)


main =
  text (Debug.toString (List.map textToShow (List.range 1 100)))
  
textToShow number = 
  if (remainderBy 15)      number == 0 then
    "FizzBuzz"
  else if (remainderBy 3)  number == 0 then
    "Fizz"
  else if (remainderBy 5)  number == 0 then
    "Buzz"
  else
    String.fromInt number
  