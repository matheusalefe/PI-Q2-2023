matriz = []
soma_p  = 0
soma_s = 0
for l in range (3):
    linha = []
    for c in range(3):
        linha.append(int(input()))
        if c == l:
            soma_p += linha[c]
        if (c+l) == 2:
            soma_s += linha[c]
    matriz.append(linha)
print(f'Soma diagonal principal: {soma_p}')
print(f'Soma diagonal secundaria: {soma_s}')
for l in range(3):
    for c in range (3):
        print(matriz[l][c], end=' ')
    print('')
