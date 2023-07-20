def comparar_matrizes(matriz1: list, matriz2: list):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False
    else:
        veredito = True
        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                if matriz2[i][j] != (matriz1[i][j] * 2):
                    veredito = False
        return veredito
