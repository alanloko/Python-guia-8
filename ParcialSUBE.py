

def verificar_transacciones(s : str) -> int:
    saldo : int = 0
    for i in s:
        if(i == "r"):
            saldo += 350
        elif(i == "v"):
            if(saldo - 56 < 0):
                break
            else:
                saldo -= 56
        elif(i == "x"):
            break
    return saldo

#print(verificar_transacciones("svsrvvvvsvvsvvv"))

def valor_minimo(s : list[(float,float)]) -> float:
    minimo : int = s[0][0]
    for i in s:
        if(i[0] < minimo):
            minimo =i[0]
    return minimo

#print(valor_minimo([(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]))

def valores_extremos(cotizacionesDiarias : dict[str,list[int,float]]) -> dict[str,(float,float)]:
    minimo : int = 0
    maximo : int = 0
    valorStock : int = 1
    PicosStock : dict[str,(float,float)] = {}
    for empresa in cotizacionesDiarias.keys():
        minimo = cotizacionesDiarias[empresa][0][valorStock]
        maximo = cotizacionesDiarias[empresa][0][valorStock]
        for dias in range(len(cotizacionesDiarias[empresa])):
            if(minimo > cotizacionesDiarias[empresa][dias][valorStock]):
                minimo = cotizacionesDiarias[empresa][dias][valorStock]
            if(maximo < cotizacionesDiarias[empresa][dias][valorStock]):
                maximo = cotizacionesDiarias[empresa][dias][valorStock]
        PicosStock[empresa] = (minimo,maximo)
    return PicosStock

#print(valores_extremos({"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}))

def es_sudoku_valido(m : list[list[int]]) -> bool:
    valido : bool = True
    numeros : list[int] = [1,2,3,4,5,6,7,8,9]
    for fila in range(len(m)):
        for index in range(len(m[0])):
            if(m[fila][index] in numeros):
                numeros.pop(posicion(m[fila][index],numeros))
            elif(m[fila][index] != 0):
                valido = False
                break
        numeros = [1,2,3,4,5,6,7,8,9]
    for columna in range(len(m)):
        for index in range(len(m[0])):
            valor = m[index][columna]
            if(valor in numeros):
                numeros.pop(posicion(m[index][columna],numeros))
            elif(valor != 0):
                valido = False
                break
        numeros = [1,2,3,4,5,6,7,8,9]
    return valido

def posicion(n : int, numeros : list[int]):
    pos : int = 0
    for i in range(len(numeros)):
        if(numeros[i] == n):
            pos = i
            break
    return pos

# matriz = [
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [9, 8, 7, 6, 4, 5, 3, 1, 1],
# [0, 0, 0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 4, 0, 0, 0],
# [0, 0, 0, 0, 6, 0, 0, 0, 0],
# [0, 0, 0, 5, 0, 0, 0, 0, 0],
# [0, 0, 4, 0, 0, 0, 0, 0, 0],
# [0, 3, 0, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# print(es_sudoku_valido(matriz))