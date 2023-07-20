matriz = []
vet = [0,0,0]
for l in range (3):
    linha = []
    for c in range(3):
        linha.append(int(input()))
        for v in range(3):
            if v == c:
                vet[v] += linha[c]
    matriz.append(linha)
for v in range (3):
    print(vet[v], end=' ')
