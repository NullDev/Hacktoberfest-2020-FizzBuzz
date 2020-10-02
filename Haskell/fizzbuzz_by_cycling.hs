-- description: FizzBuzz by cycling through patterns
--              Since the patterns will repeat  we can cycle through lists of values
--              thereby foregoing the checking of numbers like division, mod etc completely
--              [-- technically pattern until their least common Multiple is enough]
--              Since Haskell is lazy we can work on infinite lists
-- author : @sohith

makeList :: Int -> String -> [String]
makeList n str = ["" | i<-[1..(n-1)]] ++ [str]

concatLists :: [String] -> [String] -> [String]
concatLists list1 list2 = map (\x -> fst x ++ snd x) $ zip (cycle list1) (cycle list2)

fillNums :: [String] -> [String]
fillNums list1 = map (\x -> if ((snd x) == "") then (show $ fst x) else snd x) $ zip [1..] list1

customizeFizzBuzz :: [String]
customizeFizzBuzz = concatLists (makeList 5 "Fizz") (makeList 3 "Buzz")

main = do
    mapM_ putStrLn $ take 100 $ fillNums customizeFizzBuzz