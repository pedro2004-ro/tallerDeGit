f :: Int -> Int
f n | n <= 7 = n ^ 2
    | otherwise = 2 * n - 1

g :: Int -> Int
g n | mod n 2 == 0 = div n 2
    | otherwise = 3 * n + 1

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (a, b, c) = f a > g a && f b > g b && f c > g c 
