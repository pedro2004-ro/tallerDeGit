def acomodar(s: list[str]) -> list[str]:
    res: list[str] = []
    for i in s:
        if i == "UP":
            res.append(i)
    for i in s:
        if i == "LLA":
            res.append(i)

    return res

def pos_umbral(s: list[int], u: int) -> int:
    res: int = 0
    ingresos: int = 0
    i: int = 0

    while i < len(s) and ingresos <= u:
        if s[i] > 0:
            ingresos += s[i]

        if ingresos > u:
            res = i
            
        i += 1

    return res

def col(e: int, mat: list[list[int]]) -> list[int]:
    res: list[int] = []
    i: int = 0

    while i < len(mat):
        res.append(mat[i][e])
        i += 1

    return res
    
def mitades(mat: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    primera_mitad: list[list[int]] = []
    segunda_mitad: list[list[int]] = []
    i: int = 0

    while i < len(mat[0])/2:
        primera_mitad.append(col(i, mat))
        i += 1

    while i < len(mat[0]):
        segunda_mitad.append(col(i, mat))
        i += 1

    res = (primera_mitad, segunda_mitad)

    return res

def columnas_repetidas(mat: list[list[int]]) -> bool:
    return mitades(mat)[0] == mitades(mat)[1]

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int, list[str]]) -> dict[str, list[int]]:
    res: dict[str, list[int]] = {}

    for nacion in naciones:
        posiciones = [0]*len(naciones)

        for v in torneos.values():
            i: int = 0

            while i < len(v):
                if v[i] == nacion:
                    posiciones[i] += 1

                i += 1

        res[nacion] = posiciones
    
    return res



            
        