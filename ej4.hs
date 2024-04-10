prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (a, b) (c, d) = a*c + b*d

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float 
distanciaPuntos (a, b) (c, d) = ((c-a)**2 + (d-b)**2)**(0.5)

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (a, b, c) = a + b + c

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a, b, c) n = ceroSiNoMultiplo a n + ceroSiNoMultiplo b n + ceroSiNoMultiplo c n 
                               where ceroSiNoMultiplo a n | mod a n == 0 = a
                                                          | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a, b, c) | mod a 2 == 0 = 1
                       | mod b 2 == 0 = 2
                       | mod c 2 == 0 = 3
                       | otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)
