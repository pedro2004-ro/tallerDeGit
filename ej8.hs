comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos a = mod (abs a) 10 + mod (div (abs a) 10) 10
