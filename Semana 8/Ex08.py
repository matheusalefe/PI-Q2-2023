l = int(input())
c = int(input())
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(i*2+(j*l*2))
    matriz.append(linha)

for i in range(l):
    for j in range (c):
        print(f'{matriz[i][j]:.0f}', end=' ')
    print('')
