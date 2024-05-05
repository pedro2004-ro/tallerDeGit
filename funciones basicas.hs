longitud :: [t] -> Int
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso xs = ultimo xs : reverso (principio xs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y : xs) = x == y || pertenece x xs

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

maximoAux :: Integer -> Integer -> Integer
maximoAux x y | x >= y = x
              | otherwise = y

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : xs) = maximoAux x (maximo xs)