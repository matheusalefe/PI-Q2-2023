matriz = []
maior10  = 0
menor0 = 0
for l in range (4):
    linha = []
    for c in range(4):
        linha.append(int(input()))
        if linha[c] > 10:
            maior10 += 1
        elif linha[c] < 0:
                menor0 += 1
    matriz.append(linha)
print(f'Maior que 10: {maior10}')
print(f'Menor que 0: {menor0}')
for l in range(4):
    for c in range (4):
        print(matriz[l][c], end=' ')
    print('')
