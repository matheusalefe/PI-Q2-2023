def somar_vizinhos(matriz:list, linha:int, coluna:int):
    soma = 0
    for i in range (-1,2):
        for j in range(-1,2):
            soma += matriz[linha + i][coluna + j]
    soma -= matriz[linha][coluna]
    return soma

mat = [
    [1,2,3,4,5,6,7],
    [2,1,3,1,1,0,0],
    [3,1,2,2,2,1,0],
    [1,0,1,5,5,1,1],
    [1,1,1,0,1,0,0]
]
print(somar_vizinhos(mat, 2, 3))