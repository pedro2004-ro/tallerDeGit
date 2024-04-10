bisiesto :: Int -> Bool
bisiesto n | mod n 400 == 0 = True
           | mod n 100 == 0 = False
           | mod n 4 == 0 = True
           | otherwise = False