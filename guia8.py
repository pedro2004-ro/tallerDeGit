from queue import LifoQueue as Pila
import random
import csv

def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)
        
def slice(txt: str, inicio: int, final: int) -> str:
    res: str = ""
    while inicio < final:
        res = res + txt[inicio]
        inicio += 1
    return res
        
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, 'r')
    archivo_texto = archivo.read()
    res: bool = False
    i: int = 0
    while i + len(palabra) <= len(archivo_texto):
        chequeo: str = slice(archivo_texto, i, i+len(palabra))
        if chequeo == palabra:
            res = True
        i += 1
        
    archivo.close()
    return res
    
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_texto = archivo.read()
    res: int = 0
    i: int = 0
    while i + len(palabra) <= len(archivo_texto):
        chequeo: str = slice(archivo_texto, i, i+len(palabra))
        if chequeo == palabra:
            res += 1
        i += 1
        
    archivo.close()
    return res

def sacar_espacios(linea: str) -> str:
    res: str = ""
    p: bool = False
    i: int = 0
    
    for i in linea:
        if p and i == ' ':
            res += i
        if i != ' ':
            res += i
            p = True
                 
    return res

def es_comentario(linea: str) -> bool:
    return linea[0] == '#'

def clonar_sin_comentarios(nombre_archivo: str):
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo_nuevo_texto: str = ""
    
    for linea in archivo_lineas:
        if not es_comentario(linea):
            archivo_nuevo_texto += linea
            
    archivo_nuevo = open('sincomentarios.txt', 'w')
    archivo_nuevo.write(archivo_nuevo_texto)
    
    archivo_nuevo.close()
    archivo.close()
            
def borrar(s: str, d: str) -> str:
    i: int = 0
    res: str = ""
    
    while i + len(d) <= len(s):
        check: str = slice(s, i, i + len(d))
        if not d == check:
            res = res + check
            
        i += len(d)
        
    return res
            

def invertir_lineas(nombre_archivo: str):
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo_reverso_lineas = []
    i: int = len(archivo_lineas) - 1
    
    archivo_reverso_lineas.append(archivo_lineas[i] + '\n')
    i -= 1
    
    while i >= 1:
        archivo_reverso_lineas.append(archivo_lineas[i])
        i -= 1
                
    archivo_reverso_lineas.append(borrar(archivo_lineas[0], '\n'))            
                
    archivo_reverso = open('reverso.txt', 'w')
    for i in archivo_reverso_lineas:
        archivo_reverso.write(i)
        
    archivo_reverso.close()
    archivo.close()
    
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, 'r+')
    archivo_t = archivo.read()
    
    archivo_nuevo = open(nombre_archivo, 'w')
    
    archivo_t += frase
    
    archivo_nuevo.write(archivo_t)
    
    archivo_nuevo.close()
    archivo.close()
    
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, 'r')
    archivo_t = archivo.read()
    
    archivo_nuevo = open(nombre_archivo, 'w')
    
    archivo_t = frase + archivo_t
    
    archivo_nuevo.write(archivo_t)
    
    archivo_nuevo.close()
    archivo.close()
    
def listar_palabras_de_archivo(nombre_archivo: str) -> list:
    archivo = open(nombre_archivo, 'r')
    archivo_t = archivo.read()
    res: list = []
    i: int = 0
    
    while i + 5 <= len(archivo_t):
        res.append(slice(archivo_t, i, i + 5))
        i += 5
        
    res[-1] += slice(archivo_t, i, len(archivo_t))
        
    archivo.close()
    return res

def suma(lista: list) -> int:
    res: int = 0
    for i in lista:
        res += i
    return res

def pertenece(e, lista: list) -> bool:
    res: bool = False
    for i in lista:
        if e == i:
            res = True
    return res

def promedio_estudiante(nombre_archivo: str, lu: str) -> float:
    with open(nombre_archivo, 'r') as csv_archivo:
        csv_reader = csv.reader(csv_archivo)

        notas: list[int] = []
        for row in csv_reader:
            if row[0] == lu:
                notas.append(int(row[-1]))
        
        csv_archivo.close()

    return suma(notas) / len(notas)

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    with open(nombre_archivo_notas, 'r', newline='') as notas:
        csv_reader = csv.reader(notas)

        promedios_alumnos: dict = {}
        for row in csv_reader:
            alumno: str = row[0]
            if alumno != "nro lu" and not pertenece(alumno, promedios_alumnos.keys()):
                promedios_alumnos[alumno] = promedio_estudiante(nombre_archivo_notas, alumno)

        notas.close()
    
    with open(nombre_archivo_promedios, 'w', newline='') as promedios:
        fieldnames = ['alumno', 'promedio']
        csv_writer = csv.DictWriter(promedios, fieldnames=fieldnames)

        csv_writer.writeheader()
        for k in promedios_alumnos:
            v = promedios_alumnos[k]
            csv_writer.writerow({'alumno': k, 'promedio': v})
        
        promedios.close()

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila = Pila()
    for _ in range(cantidad+1):
        p.put(random.randint(desde, hasta))

    return p

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

def cantidad_elementos(p: Pila) -> int:
    pila_c: list = []

    while not p.empty():
        e = p.get()
        pila_c.append(e)

    res: int = len(pila_c)

    for i in range(len(pila_c) - 1, -1, -1):
        p.put(pila_c[i])

    return res

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

def esta_bien_balanceada(s: str) -> bool:
    cont: int = 0
    res = True

    for i in s:
        if cont < 0:
            res = False
        if i == '(':
            cont += 1
        if i == ')':
            cont -= 1
        
    if cont != 0:
        res = False

    return res

def operar(a, b, operador) -> float:
    res: float = 0

    if operador == '+':
        res = a + b
    elif operador == '-':
        res = a - b
    elif operador == '*':
        res = a * b
    elif operador == '/':
        res = a / b

    return res

def evaluar_expresion(s: str) -> float:
    operadores = ['+', '-', '*', '/']
    p = Pila()

    for i in s:
        if pertenece(i, operadores):
            a = p.get()
            b = p.get()
            p.put(operar(b, a, i))
        elif i != ' ':
            p.put(int(i))

    return p.get()

print(evaluar_expresion("3 4 + 5 * 2 -"))

    
