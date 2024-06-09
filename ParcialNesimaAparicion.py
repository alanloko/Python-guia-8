

def indice_nesima_aparicion(s : list[int], n : int, elem : int) -> int:
    apariciones : int = 0
    pos : int = -1
    for i in range(len(s)):
        if(s[i] == elem):
            apariciones += 1
            if(apariciones == n):
                pos = i
            
            
    return pos
    
# s = [1, 1, 1, 5, -7, 1, 3]
# n = 1
# elem = 1
# print(indice_nesima_aparicion(s,n,elem))

def mezclar(s1 : list[int], s2 : list[int]) -> list[int]:
    listaMezclada : list[int] = []
    for i in range(len(s1)):
        listaMezclada.append(s1[i])
        listaMezclada.append(s2[i])
    return listaMezclada

# s1 = [1, 3, 0, 1]
# s2 = [4, 0, 2, 3]
# print(mezclar(s1,s2))
    
def frecuencia_posiciones_por_caballo(caballos : list[str], carreras : dict[str,list[str]]) -> dict[str,list[int]]:
    lista_ceros = [0]*len(caballos)
    posiciones : dict[str,list[int]] = {}
    for i in caballos:
        posiciones[i] = lista_ceros.copy()
    for i in carreras.keys():
        for pos in range(len(carreras[i])):
            posiciones[carreras[i][pos]][pos] += 1
    return posiciones

# caballos= ["linda", "petisa", "mister", "luck" ]
# carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
#                   "carrera2":["petisa", "mister", "linda", "luck"]}
# print(frecuencia_posiciones_por_caballo(caballos,carreras))

def matriz_capicua(m : list[list[int]]) -> bool:
    esCapicua : bool = True
    for i in range(len(m)):
        longitud = len(m[i]) - 1
        for j in range(len(m[i])):
            if(m[i][j] != m[i][longitud]):
                esCapicua = False
                break
            longitud -= 1
    return esCapicua

m = [[1,2,2,1],[-5,6,6,-5],[1,0,0,1]]
print(matriz_capicua(m))