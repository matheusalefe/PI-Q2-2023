n = int(input())
matriz = []
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(int(input()))
    matriz.append(lista)

matriz_mult = []
for i in range(n):
    lista_multi = []
    for j in range(n):
        lista_multi.append(matriz[i][j] * matriz[j][j])
    matriz_mult.append(lista_multi)

print('Matriz Original:')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]}', end=' ')
    print('')
print('Matriz Alterada:')
for i in range(n):
    for j in range(n):
        print(f'{matriz_mult[i][j]}', end=' ')
    print('')