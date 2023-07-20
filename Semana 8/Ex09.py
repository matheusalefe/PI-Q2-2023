def criar_matriz(l:int, c:int):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            if i <= (l-1)/2:
                linha.append(11)
            else:
                linha.append(22)
        matriz.append(linha)
    return matriz
