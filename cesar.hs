import Data.Char

esMinuscula :: Char -> Bool
esMinuscula caracter = ord caracter >= ord 'a' && ord caracter <= ord 'z'

letraANatural :: Char -> Int
letraANatural caracter = ord caracter - ord 'a'

desplazar :: Char -> Int -> Char
desplazar caracter _ | not (esMinuscula caracter) = caracter
desplazar caracter n | esMinuscula c_desplazado = c_desplazado
                     | ord caracter + n > ord 'z' = desplazar caracter (n-26)
                     | otherwise = desplazar caracter (n+26)
                     where c_desplazado = (chr (ord caracter + n))

{- cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar [c] n = [desplazar c n]
cifrar (x : xs) n = desplazar x n : cifrar xs n -}

