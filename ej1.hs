f :: Int -> Int
f 1 = 8
f 4 = 131
f 16 = 16 

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

h :: Int -> Int
h n = f (g n)

k :: Int -> Int
k n = g (f n)

maximo3 :: Int -> Int -> Int -> Int
maximo3 a b c | a >= b && a >= c = a
              | b >= a && b >= c = b
              | c >= b && c >= a = c

absoluto :: Int -> Int
absoluto a | a >= 0 = a
           | a < 0 = -a

maximoabsoluto :: Int -> Int -> Int
maximoabsoluto a b | absoluto a >= absoluto b = absoluto a 
                   | absoluto b > absoluto a = absoluto b

algunoEs0 :: Int -> Int -> Bool
{- algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 _ _ = False -}

algunoEs0 a b | a == 0 || b == 0 = True
              | otherwise = False

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos a b c | a == b && b == c = 0
                    | a == b = c
                    | b == c = a 
                    | a == c = b 
                    | otherwise = a + b + c

digitoUnidades :: Int -> Int
digitoUnidades n | n >= 0 = mod n 10
                 | n < 0 = mod (-n) 10

digitoDecenas :: Int -> Int
digitoDecenas n | n >= 0 = digitoUnidades (div n 10)
                | n < 0 = digitoUnidades (div (-n) 10)

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (a, b) (c, d) = a < c && b < d 