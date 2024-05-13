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

cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar (x : xs) n = desplazar x n : cifrar xs n

descifrar :: String -> Int -> String
descifrar lista n = cifrar lista (-n)

cifrarListaAux :: [String] -> Int -> [String]
cifrarListaAux [] _ = []
cifrarListaAux (frase : frases) n = cifrar frase n : cifrarListaAux frases (n+1)


cifrarLista :: [String] -> [String]
cifrarLista frases = cifrarListaAux frases 0

contarLetra :: String -> Char -> Int
contarLetra [] _ = 0
contarLetra (letra : frase) caracter | caracter == letra = 1 + contarLetra frase caracter
                                     | otherwise = contarLetra frase caracter

contarLetrasAux :: String -> String -> [Int]
contarLetrasAux [] _ = [0]
contarLetrasAux (letra : abecedario) frase = contarLetra frase letra : contarLetrasAux abecedario frase

contarLetras :: String -> [Int] 
contarLetras frase = contarLetrasAux "abcdefghijklmnopqrstuvwxyz" frase 