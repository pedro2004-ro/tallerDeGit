import random
import numpy as np
from queue import LifoQueue as Pila
import random
import csv

def pertenece(lista: list[int], e: int) -> bool:
    res: bool = False
    for i in lista:
        if e == i:
            res = True
    return res

def suma(lista: list[int]) -> int:
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

def reverso(palabra: str) -> str:
    res: str = ""
    i: int = 1
    while i <= longitud(palabra):
        res = res + palabra[longitud(palabra)-i]
        i += 1 
    return res

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

def eliminar_repetidos_facil(s: str) -> str:
    res: str = ""
    for i in s:
        if not pertenece_char(res, i):
            res = res + i
    return res

def producto_v(a: list[float], b: list[float]) -> float:
    res: float = 0
    for i in range(0, longitud(a)):
        res += a[i] * b[i]
    return res

def col(a: list[list[float]], e: int) -> list[float]:
    res: list[float] = []

    for i in a:
        res.append(i[e])

    return res

def producto_m(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    res: list[list[float]] = []

    for i in range(0, longitud(a)):
        res.append([])
        for j in range(0, longitud(a[i])):
            res[i].append(producto_v(a[i], col(b, j)))

    return res
    
def identidad(e: int) -> list[list[float]]:
    res: list[float[float]] = []
    for i in range(0, e):
        res.append([])
        for j in range(0, e):
            if i == j:
                res[i].append(1)
            else:
                res[i].append(0)
    return res
        

def m_a_la(a: list[list[float]], e: int) -> list[list[float]]:
    res: list[list[float]] = identidad(longitud(a))
    i: int = 0

    while i < e:
        res = producto_m(res, a)
        i += 1
    
    return res

def slice(txt: str, inicio: int, final: int) -> str:
    res: str = ""
    while inicio < final:
        res = res + txt[inicio]
        inicio += 1
    return res

def insert(e, pos: int, lista: list):
    lista.append(lista[-1])
    i: int = len(lista) - 2
    while i > 0:
        if i > pos:
            lista[i] = lista[i-1]
        i -= 1

    lista[pos] = e


def escribir_pila(pila: Pila):
    pila_copy: list = []

    while not pila.empty():
        p = pila.get()
        pila_copy.append(p)

    print(pila_copy)

    for i in range(len(pila_copy)-1, -1, -1):
        pila.put(pila_copy[i])

def escribir_pila_2(pila: Pila):
    pila_c: Pila = Pila()

    while not pila.empty():
        p = pila.get()
        print(p)
        pila_c.put(p)

    while not pila_c.empty():
        p = pila_c.get()
        pila.put(p)

def cantidad_elementos_2(p: Pila) -> int:
    pila_c: Pila = Pila()
    res: int = 0
    while not p.empty():
        e = p.get()
        pila_c.put(e)
        res += 1

    while not pila_c.empty():
        e = pila_c.get()
        p.put(e)

    return res

def buscar_el_maximo(p: Pila[int]) -> int:
    res: int = p.get()
    p_copy: Pila = Pila()
    p_copy.put(res)

    while not p.empty():
        m = p.get()
        p_copy.put(m)

        if m > res:
            res = m

    while not p_copy.empty():
        a = p_copy.get()
        p.put(a)

    return res
