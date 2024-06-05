from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

## Archivos:

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


### Pilas:

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
    if(cantidad_elementos(p) % 2 != 0):
        return False
    else:    
        return cierraparentesis(p.get(),p,False)
        
def cierraparentesis(parentesis : str,p : Pila[str],closed : bool) -> bool:
    if(parentesis == '(' and p.empty()):
        closed = True
    elif(not(p.empty())):
        return cierraparentesis(p.get(),p,closed)
    return closed

#print(esta_bien_balanceada("((1 + (2 x 3 = (20 / 5))"))

def evaluar_expresion(s : str) -> float:
    pila : Pila[str]= Pila()
    cont : int = 0
    for i in range(len(s) - 1,-1,-1):
        if(s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/"):
            cont += 1
        if(s[i] != " ") :
            pila.put(s[i])
        

    while(cont != 0):
        n1 : int = float(pila.get())
        n2 : int = float(pila.get())
        op : str = pila.get()
        pila.put(operador(op,n1,n2))
        cont -= 1
    return pila.get()


def operador(s : str, n1 : int, n2 : int) -> float:
    if(s == "+"):
        return n1 + n2
    elif(s == "-"):
        return n1 - n2
    elif(s == "*"):
        return n1 * n2
    else:
        return n2 / n1
    
#print(evaluar_expresion("3 4 + 5 * 2 -"))

### Colas: 

def generar_num_al_azar(cantidad : int, desde : int, hasta : int) -> Cola[int]:
    c : Cola[int] = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde,hasta))
    return c


# c = generar_num_al_azar(5,1,10)

# while(not(c.empty())):
#      print(c.get())


def cantidadElementos(c : Cola) -> int:
    elementos : list = []
    cont : int = 0
    while(not(c.empty())):
        elementos.append(c.get())
        cont += 1
    for i in elementos:
        c.put(i)
    return cont

# c : Cola[int] = Cola()
# c.put(1)
# c.put(2)
# c.put(3)
# c.put(4)
# print(list(c.queue))
# print(cantidadElementos(c))
# print(list(c.queue))
def maximoColas(c : Cola) -> int:
    elementos : list = []
    while(not(c.empty())):
        elementos.append(c.get())
    for i in elementos:
        c.put(i)
    max : int = elementos[0]
    for elem in elementos:
        if(elem > max):
            max = elem
    return max
# c : Cola[int] = Cola()
# c.put(1)
# c.put(7)
# c.put(3)
# c.put(4)
# print(list(c.queue))
# print(maximoColas(c))
# print(list(c.queue))

def secuencia_bingo(n : int) -> Cola[int]:
    bingo : Cola[int] = Cola()
    numeros : list[int] = []
    for i in range(n):
        numeros.append(i)
    while(len(numeros) > 0):
        if(len(numeros) == 1):
            pos = 0
        else:
            pos = random.randint(0,len(numeros))
            if(pos == len(numeros)):
                pos = pos - 1 
        bingo.put(numeros[pos])
        numeros.pop(pos)
    return bingo
# bingo = secuencia_bingo(100)
# print(list(bingo.queue))

def jugar_carton_bingo(carton : list[int], bolillero : Cola[int]) -> int:
    cont : int = 0
    while(not(bolillero.empty())):
        numero : int = bolillero.get()
        if(pertenece(numero,carton)):
            carton.pop(posicion(numero,carton))
        cont += 1
        if(len(carton) == 0):
            break
    return cont
        
def pertenece(numero : int, carton : list[int]) -> int:
    for i in carton:
        if(i == numero):
            return True
    return False

def posicion(numero : int, carton : list[int]) -> int:
    for i in range(len(carton)):
        if(carton[i] == numero):
            return i
        
#  
def n_pacientes_urgentes(c : Cola[(int,str,str)]) -> int:
    elementos : list[(int,str,str)] = []
    cont : int = 0
    while(not(c.empty())):
        elementos.append(c.get())
    for i in elementos:
        c.put(i)
    for i in elementos:
        if(i[0] <= 3 and i[0] >= 1):
            cont += 1
    return cont

# c = Cola()
# c.put((10,"c","h"))
# c.put((1,"a","b"))
# c.put((3,"s","t"))
# c.put((1,"g","y"))
# c.put((7,"c","h"))
# c.put((2,"c","h"))
# c.put((6,"c","h"))

# print(n_pacientes_urgentes(c))

def atencion_clientes(c : Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
    elementos : list[(int,str,str)] = []
    clientes : Cola[(str,int,bool,bool)] = Cola()
    prioridad1 : Cola[(str,int,bool,bool)] = Cola()
    prioridad2 : Cola[(str,int,bool,bool)] = Cola()
    sinprioridad : Cola[(str,int,bool,bool)] = Cola()
    prioridades : Cola[(str,int,bool,bool)] = Cola()
    while(not(c.empty())):
        elementos.append(c.get())
    for i in elementos:
        c.put(i)
        clientes.put(i)
    while(not(clientes.empty())):
        cliente : (str,int,bool,bool) = clientes.get() # type: ignore
        if(cliente[3] == 1):
            prioridad1.put(cliente)
        elif(cliente[2] == 1):
            prioridad2.put(cliente)
        else:
            sinprioridad.put(cliente)
    while(not(prioridad1.empty())):
        cliente = prioridad1.get()
        prioridades.put(cliente)
    
    while(not(prioridad2.empty())):
        cliente = prioridad2.get()
        prioridades.put(cliente)
    while(not(sinprioridad.empty())):
        cliente = sinprioridad.get()
        prioridades.put(cliente)
    return prioridades


# clientes : Cola[(str,int,bool,bool)] = Cola()
# clientes.put(("a",1,1,1))
# clientes.put(('u', 111, 0, 1))
# clientes.put(("b",2,0,1))
# clientes.put(("c",3,1,0))
# clientes.put(("z",4,0,0))
# clientes.put(("d",5,0,1))
# clientes.put(("e",6,1,0))
# clientes.put(('t', 40, 0, 0))
# clientes.put(('h', 41, 1, 0))
# clientes.put(('i', 47, 0, 1))

# print(list(atencion_clientes(clientes).queue))

### Diccionarios: 

def agrupar_por_longitud(archivo : str) -> dict:
    archivo = open("archivo.txt", "r")
    palabras : dict = {}
    contenido = archivo.read()
    largo = 0
    for i in contenido:
        if(i == " " or i == '\n'):
            if(largo in palabras.keys()):
                palabras[largo] += 1
            else:
                palabras[largo] = 1
            largo = 0
        else:
            largo += 1
    palabras.pop(0)
    archivo.close()

    return palabras

# print(agrupar_por_longitud("archivo.txt"))

def contador_palabras(archivo : str) -> dict:
    archivo = open("archivo.txt", "r")
    palabras : dict = {}
    contenido = archivo.read()
    palabra : str = ""
    for i in contenido:
        if(i == " " or i == '\n'):
            if(palabra in palabras.keys()):
                palabras[palabra] += 1
            else:
                palabras[palabra] = 1
            palabra = ""
        else:
            palabra += i
    if(len(palabra) > 0):
        if(palabra in palabras.keys()):
                palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    palabras.pop("")
    archivo.close()
    return palabras


def palabra_con_mas_apariciones(archivo : str):
    palabras : dict = contador_palabras(archivo)
    llaves = list(palabras.keys())
    maximo = palabras[llaves[0]]
    palabra = llaves[0]
    for i in llaves:
        if(maximo < palabras[i]):
            maximo = palabras[i]
            palabra = i
    return palabra

# print(palabra_con_mas_apariciones("archivo.txt"))

historiales : dict[str,Pila[str]] = {}

def visitar_sitio(historiales : dict[str,Pila[str]], usuario : str, sitio : str) ->  None:
    pila : Pila[str] = Pila()
    if(usuario in historiales.keys()):
        historiales[usuario].put(sitio)
    else:
        pila.put(sitio)
        historiales[usuario] = pila
    return None

def navegar_atras(historiales : dict[str,Pila[str]], usuario : str) -> None:
    historiales[usuario].get()

visitar_sitio(historiales,"Usuario1","youtube.com")
visitar_sitio(historiales,"Usuario1","google.com")
visitar_sitio(historiales,"Usuario1","instagram.com")
print(list(historiales["Usuario1"].queue))
navegar_atras(historiales,"Usuario1")
print(list(historiales["Usuario1"].queue))



def agregar_producto(inventario : dict[str,dict[float,int]], nombre : str, precio : float, cantidad : int) -> None:
    precioycantidad : dict[float,int] = {precio : cantidad}
    inventario[nombre] = precioycantidad
    return None

def actualizar_stock(inventario : dict[str,dict[float,int]], nombre : str, cantidad : int) -> None:
    for i in inventario[nombre].keys():
        inventario[nombre][i] = cantidad

def actualizar_precio(inventario : dict[str,dict[float,int]], nombre : str, precio : float) -> None:
    for i in inventario[nombre].keys():
        cantidad = inventario[nombre][i] 
        inventario[nombre][i].pop()
    inventario[nombre][precio] = cantidad

def calcular_valor_inventario(inventario) -> float:
    productos : list[str]= list(inventario.keys())
    sumatotal : int = 0
    for i in productos:
        precio : list[float] = list(inventario[i].keys())
        cantidad : list[int] = inventario[i][precio[0]]
        sumatotal += precio[0]*cantidad
    return sumatotal

inventario : dict[str,dict[float,int]] = {}
agregar_producto(inventario, "Camisa", 20.0, 50) 
agregar_producto(inventario, "Pantalon", 30.0, 30) 
print(inventario)
actualizar_stock(inventario, "Camisa", 10)
print(inventario)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deberia imprimir 1100.00