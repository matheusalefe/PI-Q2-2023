def somar_vizinhos(matriz: list, linha: int, coluna: int):
    soma = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (linha != 0 and coluna != 0 and (linha + i) < len(matriz) and (coluna + j) < len(matriz[0])) \
                    or ((linha == 0 and coluna == 0) and (linha + i) >= 0 and (coluna + j) >= 0) \
                    or ((linha != 0 and coluna == 0) and (linha + i) < len(matriz) and (coluna + j) >= 0) \
                    or ((linha == 0 and coluna != 0) and (linha + i) >= 0 and (coluna + j) < len(matriz[0])):
                soma += matriz[linha + i][coluna + j]
    soma -= matriz[linha][coluna]
    return soma
