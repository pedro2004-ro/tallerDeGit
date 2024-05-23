def pertenece(lista: list[int], e: int) -> bool:
    res: bool = False
    for i in lista:
        if e == i:
            res = True
    return res

def divide_a_todos(lista: list[int], e: int) -> bool:
    res: bool = True
    for i in lista:
        if i % e != 0:
            res = False
    return res

def suma_total(lista: list[int]) -> int:
    sum: int = 0
    for i in lista:
        sum += i
    return sum

def ordenados(lista: list[int]) -> bool:
    i: int = 0
    res: bool = True
    while i < len(lista)-1:
        if lista[i] >= lista[i+1]:
            res = False
        i += 1
    return res

def longitud(lista: list) -> bool:
    res: int = 0
    for i in lista:
        res += 1
    return res

def palabras(lista: list[str]) -> bool:
    res: bool = False
    for i in lista:
        if longitud(i) > 7:
            res = True
    return res

def reverso(palabra: str) -> str:
    res: str = ""
    i: int = 1
    while i <= longitud(palabra):
        res = res + palabra[longitud(palabra)-i]
        i += 1 
    return res

def palindromo(palabra: str) -> bool:
    palabra2: str = reverso(palabra)
    return palabra == palabra2

def esMinus(caracter: str) -> bool:
    res: ord = False
    if (ord(caracter) >= ord('a') and ord(caracter) <= ord('z')) or caracter == 'ñ':
        res = True
    return res

def esMayus(caracter: str) -> bool:
    res: ord = False
    if (ord(caracter) >= ord('A') and ord(caracter) <= ord('Z')) or caracter == 'Ñ':
        res = True
    return res

def esNum(caracter: str) -> bool:
    res: ord = False
    if ord(caracter) >= ord('0') and ord(caracter) <= ord('9'):
        res = True
    return res

def tiene(tipo: str, contraseña: str) -> bool:
    res: bool = False
    if tipo == "mayus":
        for i in contraseña:
            if esMayus(i):
                res = True
    
    if tipo == "minus":
        for i in contraseña:
            if esMinus(i):
                res = True
    
    if tipo == "num":
        for i in contraseña:
            if esNum(i):
                res = True
    return res

def seguridad_contraseña(contraseña: str) -> str:
    res: str = "AMARILLA"
    if len(contraseña) < 5:
        res = "ROJA"
    if len(contraseña) > 8 and tiene("mayus", contraseña) and tiene("minus", contraseña) and tiene("num", contraseña):
        res = "VERDE"
    return res

def saldo(movimientos: list[tuple[str, int]]) -> int:
    saldo: int = 0
    for i in movimientos:
        if i[0] == "I":
            saldo += i[1]
        if i[0] == "R":
            saldo -= i[1]
    return saldo

def pertenece_char(lista: list[str], caracter: str) -> bool:
    res: bool = False
    for i in lista:
        if i == caracter:
            res = True
    return res

def es_vocal(letra: str) -> bool:
    res: bool = False
    if pertenece_char("aAeEiIoOuU", letra):
        res = True
    return res

def pertenece_char_sin_minus(lista: list[str], caracter: str) -> bool:
    res: bool = False
    if esMinus(caracter):
        caracterMayus: str = chr(ord(caracter) - 32)
        res = pertenece_char(lista, caracter) or pertenece_char(lista, caracterMayus)
    if esMayus(caracter):
        caracterMinus: str = chr(ord(caracter) + 32)
        res = pertenece_char(lista, caracter) or pertenece_char(lista, caracterMinus)
    else:
        res = pertenece_char(lista, caracter)
    return res

def contar_vocales_distintas(palabra: str) -> int:
    vocales: list[str] = []
    for i in palabra:
        if es_vocal(i) and not pertenece_char_sin_minus(vocales, i):
            vocales.append(i)
    return longitud(vocales)
    
def vocales_3(palabra: str) -> bool:
    return contar_vocales_distintas(palabra) >= 3

def borrar_pares(lista: list[int]):
    i: int = 0
    while i < longitud(lista):
        lista[i] = 0
        i += 2

def borrar_pares_in(lista: list[int]) -> list[int]:
    i: int = 0
    res: list[int] = []
    while i < longitud(lista):
        res.append(0)
        i += 1
        res.append(lista[i])
        i += 1
    return res

def borrar_vocales(palabra: str) -> str:
    res: str = ""
    for i in palabra:
        if es_vocal(i):
            res = res
        else:
            res = res + i
    return res

def reemplaza_vocales(s: str) -> str:
    res: str = ""
    for i in s:
        if pertenece_char("aeiou", i):
            res = res + "-"
        else:
            res = res + i
    return res

def da_vuelta(s: str) -> str:
    return reverso(s)

def slice(palabra: str, i: int) -> str:
    res: str = ""
    while i < longitud(palabra):
        res = res + palabra[i]
        i += 1
    return res

def quitar_todos(s: str, c: str) -> str:
    res: str = ""
    for i in s:
        if i == c:
            res = res
        else:
            res = res + i
    return res

def eliminar_repetidos(s: str) -> str:
    res: str = ""
    i: int = 0
    while i < longitud(s):
        if pertenece_char(slice(s, i+1), s[i]):
            res = res
        else:
            res = res + s[i]
        i += 1
    return res

def eliminar_repetidos_facil(s: str) -> str:
    res: str = ""
    for i in s:
        if not pertenece_char(res, i):
            res = res + i
    return res

def promedio(lista: list[int]) -> float:
    return suma_total(lista) / longitud(lista)

def aplazo(notas: list[int]) -> bool:
    res: bool = False
    for i in notas:
        if i < 4:
            res = True
    return res

def aprobado(notas: list[int]) -> int:
    res: int = 0

    if aplazo(notas):
        res = 3
    elif promedio(notas) > 7:
        res = 1
    else:
        res = 2
    return res

def estudiantes() -> list[str]:
    res: list[str] = []
    estudiante: str = input("Ingrese estudiante: ")
    while estudiante != "listo":
        res.append(estudiante)
        estudiante = input("Ingrese estudiante: ")
    return res

print(estudiantes())