

def ultima_aparicion(s : list[int], e : int) -> int:
    pos : int = 0
    for i in range(len(s)):
        if(s[i] == e):
            pos = i
    return pos

#print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0))

def elementos_exclusivos(s : list[int], t : list[int]) -> list[int]:
    exclusivos : list[int] = []
    for i in s:
        if(not(i in t) and not(i in exclusivos)):
            exclusivos.append(i)
    for j in t:
        if(not(j in s) and not(j in exclusivos)):
            exclusivos.append(j)
    return exclusivos

# s = [-1,4,0,4,3,0,100,0,-1,-1]
# t = [0,100,5,0,100,-1,5]
# print(elementos_exclusivos(s,t))

def contar_traducciones_iguales(ing : dict[str,str], ale : dict[str,str]) -> int:
    iguales : int = 0
    for i in ing.keys():
        for j in ale.keys():
            if(ing[i] == ale[j]):
                iguales += 1
    return iguales

# aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Hola"}
# ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand","papa" : "Hola"}
# print(contar_traducciones_iguales(ingles,aleman))

def convertir_a_diccionario(s : list[int]) -> dict[int,int]:
    apariciones : dict[int,int] = {}
    for i in s:
        if(i in apariciones.keys()):
            apariciones[i] += 1
        else:
            apariciones[i] = 1
    return apariciones

#print(convertir_a_diccionario([1,2,1,1,2,1]))