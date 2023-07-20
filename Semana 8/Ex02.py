n = int(input())
matriz = []
for l in range(n):
    lista = []
    for c in range(n):
        if l == c:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)

for l in range(n):
    for c in range (n):
        print(matriz[l][c], end=' ')
    print('')
