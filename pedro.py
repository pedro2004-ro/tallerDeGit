def pertenece(lista: list[int], e: int) -> bool:
    for i in lista:
        if e == i:
            return True
    return False

def divide_a_todos(lista: list[int], e: int) -> bool:
    for i in lista:
        if i % e != 0:
            return False
    return True

def suma_total(lista: list[int]) -> int:
    sum: int = 0
    for i in lista:
        sum += i
    return sum

def ordenados(lista: list[int]) -> bool:
    i: int = 0
    while i < len(lista)-1:
        if lista[i] >= lista[i+1]:
            return False
        i += 1
    return True

def palabras(lista: list[str]) -> bool:
    for i in lista:
        if len(i) > 7:
            return True
    return False

def palindromo(palabra: str) -> bool:
    palabra2 = palabra[::-1]
    return palabra == palabra2

def tiene(tipo: str, contraseña: str) -> bool:
    if tipo == "mayus":
        for i in contraseña:
            if i.isupper():
                return True
        return False
    
    if tipo == "minus":
        for i in contraseña:
            if i.islower():
                return True
        return False
    
    if tipo == "num":
        for i in contraseña:
            if i.isnumeric():
                return True
        return False

def seguridad_contraseña(contraseña: str) -> str:
    if len(contraseña) < 5:
        return "ROJA"
    if len(contraseña) > 8 and tiene("mayus", contraseña) and tiene("minus", contraseña) and tiene("num", contraseña):
        return "VERDE"
    return "AMARILLA"

print(seguridad_contraseña("hooAaaaaaaaaaaa7"))