n = int(input())
matriz = []
for i in range(n):
    lista = []
    for j in range(2):
        lista.append(int(input()))
    matriz.append(lista)

vet = []
for i in range(n):
    vet.append((matriz[i][0] * matriz[i][1])/2)

print('Matriz:')
for i in range(n):
    for j in range(2):
        print(f'{matriz[i][j]}', end=' ')
    print('')

print('Vetor:')
for i in range(n):
    print(f'{vet[i]}', end=' ')