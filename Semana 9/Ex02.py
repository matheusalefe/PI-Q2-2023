n = int(input())
m = int(input())
mat_o = []
mat_a = []
vet_i = []
vet_p = []
for i in range(n):
    lista_o = []
    lista_a = []
    for j in range(m):
        lista_o.append(int(input()))
        lista_a.append(lista_o[j])
        if i % 2 == 1 and lista_o[j] % 2 == 0:
            vet_p.append(lista_o[j])
            lista_a[j] = 1
        elif i % 2 == 0 and lista_o[j] % 2 == 1:
            vet_i.append(lista_o[j])
            lista_a[j] = 2
    mat_o.append(lista_o)
    mat_a.append(lista_a)

print('Matriz Original:')
for i in range(n):
    for j in range(m):
        print(f'{mat_o[i][j]}', end=' ')
    print('')

print('Matriz Alterada:')
for i in range(n):
    for j in range(m):
        print(f'{mat_a[i][j]}', end=' ')
    print('')

print('Vet_p:')
for i in range(len(vet_p)):
    print(vet_p[i], end=' ')
print('')

print('Vet_i:')
for i in range(len(vet_i)):
    print(vet_i[i], end=' ')
print('')
