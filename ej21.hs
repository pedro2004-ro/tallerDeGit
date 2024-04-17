pitagorasAux :: Integer -> Integer -> Integer -> Integer
pitagorasAux n m r | n == 0 && m ^ 2 <= r ^ 2 = 1
                   | n == 0 = 0
                   | n ^ 2 + m ^ 2 > r ^ 2 = pitagorasAux (n-1) m r
                   | n ^ 2 + m ^ 2 <= r ^ 2 = 1 + pitagorasAux (n-1) m r
                   | otherwise = -100000


pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras n 0 r = pitagorasAux n 0 r
pitagoras n m r = pitagorasAux n m r + pitagoras n (m-1) r


