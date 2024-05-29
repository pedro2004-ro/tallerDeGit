from queue import LifoQueue as Pila
import random

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