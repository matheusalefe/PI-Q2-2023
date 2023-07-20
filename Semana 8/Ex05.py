matriz = []
soma_p  = 0
soma_s = 0
vet = [0,0,0]
for l in range (3):
    linha = []
    for c in range(3):
        linha.append(int(input()))
        for v in range(3):
            if v == c:
                vet[v] += linha[c]
    matriz.append(linha)
print(f'Soma diagonal principal: {soma_p}')
print(f'Soma diagonal secundaria: {soma_s}')
for v in range (3):
    print(vet[v], end=' ')
