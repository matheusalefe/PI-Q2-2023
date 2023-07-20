n = int(input())
matriz = []
prod_s = 1
for l in range (n):
    linha = []
    for c in range(n):
        linha.append(int(input()))
        if (c+l) == (n-1):
            prod_s *= linha[c]
    matriz.append(linha)
print(f'O produto eh: {prod_s}')
