--author : @mainak-debnath
module Main where
main :: IO ()
main = printAll $ map fizzBuzz [1..100]
 where
 printAll [] = return ()
 printAll (x:xs) = putStrLn x >> printAll xs
fizzBuzz :: Integer -> String
fizzBuzz n | n `mod` 15 == 0 = "FizzBuzz"
 | n `mod` 5 == 0 = "Fizz"
 | n `mod` 3 == 0 = "Buzz"
 | otherwise = show n