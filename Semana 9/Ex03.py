n = int(input())
m = int(input())
mat = []
vet_a = []
vet_b = []
for i in range(n):
    lista = []
    for j in range(m):
        lista.append(int(input()))
    mat.append(lista)

for i in range(m):
    col_min = mat[0][i]
    col_max = mat[0][i]
    for j in range(n):
        if mat[j][i] < col_min:
            col_min = mat[j][i]
        if mat[j][i] > col_max:
            col_max = mat[j][i]
    vet_a.append(col_max)
    vet_b.append(col_min)
 
soma_vet_a = 0
soma_vet_b = 0

for c in range(m):
    soma_vet_a += vet_a[c]
    soma_vet_b += vet_b[c]

media_vet_a = soma_vet_a/m
media_vet_b = soma_vet_b/m

print('mat:')
for i in range(n):
    for j in range(m):
        print(f'{mat[i][j]}', end=' ')
    print('')

print('vet_A:')
for i in range(len(vet_a)):
    print(vet_a[i], end=' ')
print('')
print(f'Media de vet_A: {media_vet_a:.2f}')
print('vet_B:')
for i in range(len(vet_b)):
    print(vet_b[i], end=' ')
print('')
print(f'Media de vet_B: {media_vet_b:.2f}')
