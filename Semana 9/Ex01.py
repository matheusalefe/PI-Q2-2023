n = int(input())
m = int(input())
mat = []
soma_n = 0
soma_p = 0
for i in range(n):
    lista = []
    for j in range(m):
        lista.append(float(input()))
        if lista[j] > 0:
            soma_p += lista[j]
        else:
            soma_n += lista[j] 
    mat.append(lista)

for i in range(n):
    for j in range(m):
        print(f'{mat[i][j]:.2f}', end=' ')
    print('')

print(f'Soma Positivos: {soma_p:.2f}')
print(f'Soma Negativos: {soma_n:.2f}')
