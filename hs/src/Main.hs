module Main where

import A2019.Day1

run_191 :: IO ()
run_191 = do
  r <- compute_part1 "data/2019/day1/input"
  putStr "Compute part 1: "
  putStrLn $ show r

run :: String -> String -> IO ()
run "2019" "1" = run_191
run _ _ = putStrLn "Not defined"

main :: IO ()
main = do
  putStr "Year"
  year <- getLine
  putStrLn $ " " ++ (show year)
  putStr "Day"
  day <- getLine
  putStrLn $ " " ++ (show day)
  run year day
