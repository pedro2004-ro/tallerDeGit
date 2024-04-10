estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b | mod a b == 0 = True
                      | otherwise = False