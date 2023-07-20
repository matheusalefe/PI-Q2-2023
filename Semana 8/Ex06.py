n = int(input())
matriz = []
for l in range(n):
    lista = []
    for c in range(n):
        lista.append((c+1)+(l*n))
    matriz.append(lista)

for l in range(n):
    for c in range (n):
        print(matriz[l][c], end=' ')
    print('')
