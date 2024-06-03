from queue import LifoQueue as Pila
from queue import Queue as Cola

import random

#archivo = open("archivo.txt","r")
nuevoarchivo = open("nuevoarchivo.txt",'w')
def contarlineas(archivo : str) -> int:
    cont = 0
    contenido = archivo.readline()
    while(contenido != ''):
        cont += 1
        contenido = archivo.readline()
    archivo.close
    return cont

#print(contarlineas(archivo))

def existepalabra(palabra : str , archivo : str) -> bool:
    contenido = archivo.read()
    existe = False
    aux = ""
    for i in contenido:
        if(i == ' ' or i == '\n'):
            if(palabra == aux):
                existe = True
            aux = ""
        else:
            aux += i
    archivo.close()
    return existe
# print(existepalabra("hola",archivo))

def cantidadDeApariciones(palabra : str, archivo : str) -> int:
    contenido = archivo.read()
    cont = 0
    aux = ""
    for i in contenido:
        if(i == ' ' or i == '\n'):
            if(palabra == aux):
                cont += 1
            aux = ""
        else:
            aux += i
    archivo.close()
    return cont

# archivo = open("texto","r")
# print(cantidadDeApariciones("hola",archivo))

def escomentario(contenido : str) -> bool:
    for i in contenido:
        if(i != ' ' and i != '#'):
            return False
        elif(i == '#'):
            return True
    return False    
    

def clonarSinComentarios(archivo : str) -> str:
    contenido = archivo.readline()
    archivoNuevo = ""
    while(contenido != ''):
        if(not(escomentario(contenido))):
            archivoNuevo += contenido
        contenido = archivo.readline()
    return archivoNuevo


#nuevoarchivo.write(clonarSinComentarios(archivo))

def invertir_lineas(archivo : str) -> str:
    contenido : list[str] = []
    archivoNuevo : str = ""
    longitud = contarlineas(archivo)
    archivo = open("archivo.txt",'r')
    for i in range(longitud):
        contenido.append(archivo.readline())

    for i in range(len(contenido) - 1,-1,-1):
        archivoNuevo += contenido[i]

    return archivoNuevo

#nuevoarchivo.write(invertir_lineas(archivo))

def agregar_frase_al_final(archivo : str, frase : str):
    nuevoArchivo = archivo.read()
    nuevoArchivo += frase
    return nuevoArchivo
# frasenueva = agregar_frase_al_final(archivo,"esto es una nueva frase")
# archivo.close()
# archivo = open("archivo.txt","w")
# archivo.write(frasenueva)

def agregar_frase_al_principio(archivo : str, frase : str):
    nuevoArchivo = frase
    nuevoArchivo += "\n"
    nuevoArchivo += archivo.read()
    return nuevoArchivo

# frasenueva = agregar_frase_al_principio(archivo,"esto es una nueva frase")
# archivo.close()
# archivo = open("archivo.txt","w")
# archivo.write(frasenueva)

# archivobytes = open("archivo.txt","rb")
# bites = archivobytes.readline()
# print(chr(bites[0]))

# estudiantes = open("estudiantes.csv","r")
# contenido : str = estudiantes.readline()
# i : int= 0
# categoria : str= ""
# categorias : list[str]= []

# def promedioDeEstudiantes(archivo : str):
#     contendio = archivo.read()
#     categorias = ['Id', 'Materia', 'Fecha','Notas']
#     alumnno : list = []
#     categoria : str= ""
#     longitud = contarlineas(archivo)
#     archivo = open("estudiantes.csv",'r')
#     for i in range(longitud): 
#         while(contenido[i] != "\n"):
#             if(contendio[i] != ","):
#                 categoria += contenido[i]
#             else: 
#                 alumnno.append(categoria)
#                 categoria = ""
#         alumnno.append(categoria)
        
def generar_num_al_azar(cantidad : int, desde : int, hasta : int) -> Pila[int]:
    p = Pila()
    for i in range(cantidad):
        p.put(random.randint(desde,hasta))
    return p

# p = generar_num_al_azar(5,1,10)

# while(not(p.empty())):
#      print(p.get())

def cantidad_elementos(p : Pila) -> int:
    elementos : list = []
    cont : int = 0
    while(not(p.empty())):
        elementos.append(p.get())
        cont += 1
    for i in range(len(elementos) - 1,-1,-1):
        p.put(elementos[i])
    return cont

# print(cantidad_elementos(p))
# while(not(p.empty())):
#      print(p.get())


def buscar_el_maximo(p : Pila) -> int:
    elementos : list[int] = []
    while(not(p.empty())):
        elementos.append(p.get())
    for i in range(len(elementos) - 1,-1,-1):
        p.put(elementos[i])
    maximo : int = elementos[0]
    for elem in elementos:
        if(elem > maximo):
            maximo = elem
    return maximo
# p : Pila[int] = Pila()
# p.put(1)
# p.put(6)
# p.put(7)
# p.put(4)
# print(buscar_el_maximo(p))

def esta_bien_balanceada(s : str) -> bool:
    p : Pila[str] = Pila()
    for i in s:
        if(i == '('):
            p.put(i)
        elif(i == ')'):
            p.put(i)
    while(not(p.empty())):
        
# def cierraparentesis(p : Pila) -> bool:
#     closed = False
#     parentesis = p.get()
#     if(parentesis == '('):
#         return False
#     else:
#         cierraparentesis(p)

def generar_num_al_azar(cantidad : int, desde : int, hasta : int) -> Cola[int]:
    c : Cola[int] = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde,hasta))
    return c


# c = generar_num_al_azar(5,1,10)

# while(not(c.empty())):
#      print(c.get())
