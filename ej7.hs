distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (d, e, f) = abs (a - d) + abs (b - e) + abs (c - f)
                                       where abs x | x >= 0 = x
                                                   | x < 0 = -x