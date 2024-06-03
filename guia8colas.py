from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    q = Cola()
    for i in range(0, cantidad+1):
        n = random.randint(desde, hasta)
        q.put(n)
    
    return q

def cantidad_elementos(c: Cola) -> int:
    res: int = 0
    t: Cola = Cola()
    while not c.empty():
        a = c.get()
        t.put(a)
        res += 1

    while not t.empty():
        b = t.get()
        c.put(b)

    return res

def buscar_el_maximo(c: Cola) -> int:
    res: int = c.get()
    d = Cola()
    d.put(res)

    while not c.empty():
        a = c.get()
        if a > res:
            res = a

        d.put(a)

    while not d.empty():
        b = d.get()
        c.put(b)

    return res

def armar_secuencia_bingo() -> Cola[int]:
    a = []
    for i in range(0, 100):
        a.append(i)
    
    random.shuffle(a)

    c: Cola = Cola()
    for i in a:
        c.put(i)

    return c


def pertenece(e, lista):
    for i in lista:
        if e == i:
            return True
    return False

def quitar(e, lista):
    a = False
    for i in range(len(lista)-1):
        if lista[i] == e:
            a = True

        if a:
            lista[i] = lista[i+1]

    lista.pop()


def jugar_al_bingo(carton: list[int], bolillero: Cola) -> int:
    bolillero2 = []
    carton2 = carton
    res: int = 0

    while len(carton) > 0:
        bola = bolillero.get()
        bolillero2.append(bola)
        if pertenece(bola, carton):
            quitar(bola, carton)
        
        res += 1

    while not bolillero.empty():
        b = bolillero.get()
        bolillero2.append(b)

    for i in range(len(bolillero2)):
        bolillero.put(bolillero2[i])

    carton = carton2
    return res


def escribir_cola(c: Cola):
    temp = []
    while not c.empty():
        a = c.get()
        temp.append(a)

    for i in temp:
        c.put(i)

    print(temp)

def n_pacientes_urgentes(c: Cola) -> int:
    copia = []
    res: int = 0

    while not c.empty():
        paciente = c.get()
        if paciente[0] <= 3:
            res += 1

        copia.append(paciente)

    for i in copia:
        c.put(i)

    return res

