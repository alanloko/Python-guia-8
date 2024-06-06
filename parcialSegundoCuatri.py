

def acomodar(s : list[str]) -> list[str]:
    aux : list[str] = s.copy()
    res : list [str] = []
    for i in aux:
        if(i == "UP"):
            res.append(i)
    for i in aux:
        if(i == "LLA"):
            res.append(i)
    return res

print(acomodar(["LLA", "UP", "LLA", "LLA", "UP"]))

def pos_umbral(s : list[int], u : int):
    sumatotal : int = 0
    for i in range(len(s)):
        if(s[i] > 0):
            sumatotal += s[i]
        if(sumatotal > u):
            pos : int = i
            break
    return pos

print(pos_umbral([1,-2,0,5,-7,3],5))

def columnas_repetidas(mat : list[list[int]]):
    longitud : int = int(len(mat[0]) / 2)
    sonIguales : bool = True
    for i in range(len(mat)):
        for j in range(longitud):
            if(mat[i][j] != mat[i][j+longitud]):
                sonIguales = False
    return sonIguales

print(columnas_repetidas([[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]))

def posiciones_por_naciones(naciones : list[str], torneos : dict[int,list[str]]):
    lista_ceros = [0]*len(naciones)
    posiciones : dict[str,list[int]] = {}
    for i in naciones:
        posiciones[i] = lista_ceros.copy()
    for año in torneos.keys():
        for equipo in range(len(torneos[año])):
            pos : int = buscar_posicion(torneos[año][equipo],naciones)
            posiciones[naciones[pos]][equipo] += 1
    return posiciones

def buscar_posicion(s : str, naciones : list[str]) -> int:
    for i in range(len(naciones)):
        if(naciones[i] == s):
            return i
    

naciones = ["arg", "aus", "nz", "sud","a","b","c"]
torneos = {2023 : ["arg", "sud", "nz", "aus","a","b","c"], 2022 : ["arg","b","c","nz", "sud", "aus", "a"]}
print(posiciones_por_naciones(naciones,torneos))