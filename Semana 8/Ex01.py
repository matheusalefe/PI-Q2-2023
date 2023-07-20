matriz = []
maior  = 0
menor = 0
maior_coord = [0,0]
menor_coord = [0,0]
for l in range (3):
    linha = []
    for c in range(3):
        linha.append(int(input()))
        if l == 0 and c == 0:
            maior = linha[0]
            menor = linha[0]
        else:
            if maior < linha[c]:
                maior = linha[c]
                maior_coord = [l, c]
            elif menor > linha[c]:
                menor = linha[c]
                menor_coord = [l, c]
    matriz.append(linha)
print(f'Maior: {maior}')
print(f'Posicao (maior): {maior_coord[0]} linha e {maior_coord[1]} coluna')
print(f'Menor: {menor}')
print(f'Posicao (menor): {menor_coord[0]} linha e {menor_coord[1]} coluna')
for l in range(3):
    for c in range (3):
        print(matriz[l][c], end=' ')
    print('')
