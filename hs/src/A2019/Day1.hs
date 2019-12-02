module A2019.Day1
  ( compute_part1
  ) where

compute_fuel :: Int -> Int
compute_fuel mass = (div mass 3) - 2

read_data :: FilePath -> IO [Int]
read_data path = fmap (compute_fuel . readInt) . lines <$> readFile path
  where
    readInt :: String -> Int
    readInt = read

compute_part1 :: FilePath -> IO Int
compute_part1 = fmap (foldl (+) 0) . read_data

compute_fuel_part2 :: Int -> Int
compute_fuel_part2 mass =
  if fuel <= 0
    then 0
    else (compute_fuel_part2 fuel) + fuel
  where
    fuel = (div mass 3) - 2
-- compute_part2 :: FilePath -> IO Int
 --     fuel = (div mass 3) - 2
-- compute :: Int -> Int
-- compute mass
--   | fuel <= 0 = 0
--   | otherwise = (compute fuel) + fuel
--   where
--main :: IO ()
--main = do
--  putStrLn "Result one"
--    --- result <- (compute_part1 "data/2019/day1/input")
