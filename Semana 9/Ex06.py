n = int(input())
while n <= 4 or n % 2 == 1:
    print('Matriz Invalida!')
    n = int(input())

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == 0 or j == 0 or  i == (n-1) or j == (n-1):
            linha.append(1)
        elif (i == (n - 2)/2 and j == (n-2)/2) or (i == n/2 and j == (n - 2)/2) or (i == (n - 2)/2 and j == n/2) or (i == n/2 and j==n/2):
            linha.append(0)
        else:
            linha.append(2)
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=' ')
    print('')