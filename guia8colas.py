from queue import Queue as Cola
import random
import typing

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

def n_clientes_urgentes(c: Cola) -> int:
    copia = []
    res: int = 0

    while not c.empty():
        cliente = c.get()
        if cliente[0] <= 3:
            res += 1

        copia.append(cliente)

    for i in copia:
        c.put(i)

    return res

def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    prioridad: Cola[tuple[str, int, bool, bool]] = Cola()
    preferencial: Cola[tuple[str, int, bool, bool]] = Cola()
    resto: Cola[tuple[str, int, bool, bool]] = Cola()
    res: Cola[tuple[str, int, bool, bool]] = Cola()

    cola_back = []

    while not c.empty():
        cliente = c.get()
        cola_back.append(cliente)
        
        if cliente[3]:
            prioridad.put(cliente)
        elif cliente[2]:
            preferencial.put(cliente)
        else:
            resto.put(cliente)

    while not prioridad.empty():
        cliente = prioridad.get()
        res.put(cliente)

    while not preferencial.empty():
        cliente = preferencial.get()
        res.put(cliente)

    while not resto.empty():
        cliente = resto.get()
        res.put(cliente)

    for i in cola_back:
        c.put(i)

    return res

def separar_palabras(s: str, c: str) -> list[str]:
    i: int = 0
    res: list[str] = []
    palabra: str = ""

    while i < len(s):
        if s[i] != c:
            palabra += s[i]
        else:
            res.append(palabra)
            palabra = ""

        i += 1

    res.append(palabra)

    return res

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo: typing.IO = open(nombre_archivo, 'r')
    archivo_texto: str = archivo.read()
    archivo.close()
    res: dict = {}

    palabras: list[str] = separar_palabras(archivo_texto, " ")

    for i in palabras:
        if pertenece(len(i), res.keys()):
            res[len(i)] += 1
        else:
            res[len(i)] = 1

    return res

def parsear_csv(nombre_archivo_notas: str) -> list[list]:
    archivo: typing.IO = open(nombre_archivo_notas, 'r')
    archivo_t: str = archivo.read()
    archivo.close()
    res: list[list] = []

    lineas = separar_palabras(archivo_t, '\n')
    
    for linea in lineas:
        campos = separar_palabras(linea, ',')
        res.append(campos)

    return res

def promedio(s: list[str]) -> float:
    suma = 0

    for i in s:
        suma += float(i)

    return suma / len(s)

def notas_estudiantes(nombre_archivo_notas: str) -> dict[str, list[str]]:
    notas = parsear_csv(nombre_archivo_notas)
    res: dict[str, list[float]] = {}

    for nota in notas:
        if pertenece(nota[0], res.keys()):
            res[nota[0]].append(nota[3])
        else:
            res[nota[0]] = [nota[3]]

    return res

def calcular_promedio_por_estudiante(nombre_archivo_notas: str) -> dict[str, float]:
    notas = notas_estudiantes(nombre_archivo_notas)
    res: dict[str, float] = {}

    for k, v in notas.items():
        res[k] = promedio(v)

    return res

def palabra_mas_frecuente(nombre_archivo: str):
    return 0