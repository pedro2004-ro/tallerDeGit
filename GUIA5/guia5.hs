longitud :: [t] -> Int
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x : xs) = x : principio xs

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso xs = ultimo xs : reverso (principio xs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y : xs) = x == y || pertenece x xs

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x : y : xs) = x == y && todosIguales (y : xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x : xs) = not (pertenece x xs)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos xs = not (todosDistintos xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (y : xs) | x == y = xs
                  | otherwise = y : quitar x xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x (y : xs) | x == y = quitarTodos x xs
                       | otherwise = y : quitarTodos x xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x : xs) = x : eliminarRepetidos (quitarTodos x xs)

estaIncluido :: (Eq t) => [t] -> [t] -> Bool
estaIncluido [] [] = True
estaIncluido [x] ys = pertenece x ys
estaIncluido (x : xs) ys = pertenece x ys && estaIncluido xs ys

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = estaIncluido xs ys && estaIncluido ys xs

capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverso xs

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x : xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x : xs) = x * productoria xs

maximoAux :: Integer -> Integer -> Integer
maximoAux x y | x >= y = x
              | otherwise = y

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : xs) = maximoAux x (maximo xs) 

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [(x + n)]
sumarN n (x : xs) = (x + n) : sumarN n xs

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [(2*x)]
sumarElPrimero (x : xs) = sumarN x (x : xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo xs = sumarN (ultimo xs) xs

pares :: [Integer] -> [Integer]
pares [x] | mod x 2 == 0 = [x]
          | otherwise = []
pares (x : xs) | mod x 2 == 0 = x : pares xs
               | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [x] | mod x n == 0 = [x]
                   | otherwise = []
multiplosDeN n (x : xs) | mod x n == 0 = x : multiplosDeN n xs
                        | otherwise = multiplosDeN n xs

ordenarDecreciente :: [Integer] -> [Integer]
ordenarDecreciente [] = []
ordenarDecreciente [x] = [x]
ordenarDecreciente xs = maximo xs : ordenarDecreciente (quitar (maximo xs) xs)

ordenar :: [Integer] -> [Integer]
ordenar xs = reverso (ordenarDecreciente xs)

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos [x, y] | x == ' ' && y == ' ' = [' ']
                             | otherwise = [x, y]
sacarBlancosRepetidos (x : y : xs) | x == ' ' && y == ' '  = sacarBlancosRepetidos (x : xs)
                                   | otherwise = x : sacarBlancosRepetidos (y : xs)

contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras [x] | x == ' ' = 0
                   | otherwise = 1
contarPalabras [x, y] | x == ' ' && y == ' ' = 0
                      | otherwise = 1
contarPalabras (x : y : xs) | x /= ' ' && y == ' ' = 1 + contarPalabras (y : xs)
                            | otherwise = contarPalabras (y : xs)


nPalabra :: Int -> [Char] -> [Char]
nPalabra _ [] = []
nPalabra _ [x] = [x]
nPalabra 1 (x : xs) | x == ' ' = nPalabra 1 xs
                    | head xs /= ' ' = x : nPalabra 1 xs
                    | head xs == ' ' = [x]
nPalabra n (x : xs) | x == ' ' = nPalabra n xs
                    | head xs /= ' ' = nPalabra n xs
                    | head xs == ' ' = nPalabra (n-1) xs


rangoPalabras :: Int -> Int -> [Char] -> [[Char]]
rangoPalabras n m xs | n == m = [nPalabra n xs]
                     | otherwise = [nPalabra n xs] ++ rangoPalabras (n+1) m xs

palabras :: [Char] -> [[Char]]
palabras [] = [[]]
palabras xs = rangoPalabras 1 (contarPalabras xs) xs

maximaLongitud :: [[Char]] -> [Char]
maximaLongitud [[x]] = [x]
maximaLongitud [xs, ys] | longitud xs >= longitud ys = xs
                        | otherwise = ys
maximaLongitud (x : xs) | longitud x >= longitud (head xs) = maximaLongitud (x : tail xs)
                        | otherwise = maximaLongitud xs

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga st = maximaLongitud (palabras st)