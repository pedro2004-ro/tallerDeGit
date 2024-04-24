-- problema relacionesValidas
tuplasSonIguales :: ([Char], [Char]) -> ([Char], [Char]) -> Bool
tuplasSonIguales (a, b) (c, d) = (a == c && b == d) || (a == d && b == c)

tuplaValida :: ([Char], [Char]) -> Bool
tuplaValida (a, b) = not (a == b)

pertenece :: ([Char], [Char]) -> [([Char], [Char])] -> Bool
pertenece x [] = False
pertenece (a, b) ((c, d) : xs) = tuplasSonIguales (a, b) (c, d) || pertenece (a, b) xs

relacionesValidas :: [([Char],[Char])] -> Bool
relacionesValidas [] = True
relacionesValidas (x : xs) = not (pertenece x xs) && tuplaValida x && relacionesValidas xs

-- problema personas
perteneceATuplas :: [Char] -> [([Char], [Char])] -> Bool
perteneceATuplas x [] = False
perteneceATuplas x ((a, b) : xs) = x == a || x == b || perteneceATuplas x xs

personas :: [([Char], [Char])] -> [[Char]]
personas [] = []
personas ((a, b) : xs) | perteneceATuplas a xs && perteneceATuplas b xs = personas xs
                       | perteneceATuplas a xs = b : personas xs
                       | perteneceATuplas b xs = a : personas xs
                       | otherwise = a : b : personas xs

-- problema amigosDe
amigosDe :: [Char] -> [([Char], [Char])] -> [[Char]]
amigosDe persona [] = []
amigosDe persona ((a, b) : xs) | persona == a = b : amigosDe persona xs
                               | persona == b = a : amigosDe persona xs
                               | otherwise = amigosDe persona xs

-- problema personaConMasAmigos
longitud :: [t] -> Integer
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

cantAmigos :: [Char] -> [([Char], [Char])] -> Integer
cantAmigos persona relaciones = longitud (amigosDe persona relaciones)

personaConMasAmigosAux :: [[Char]] -> [([Char], [Char])] -> [Char]
personaConMasAmigosAux [x] _ = x
personaConMasAmigosAux (x : lista) relaciones | cantAmigos x relaciones >= cantAmigos (head lista) relaciones = personaConMasAmigosAux (x : (tail lista)) relaciones
                                              | otherwise = personaConMasAmigosAux lista relaciones

personaConMasAmigos :: [([Char], [Char])] -> [Char]
personaConMasAmigos relaciones = personaConMasAmigosAux (personas relaciones) relaciones