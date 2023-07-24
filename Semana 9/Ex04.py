n = int(input())
vet = []
mat = []
qtd_igual = 0
qtd_menores = 0
for i in range(n):
    vet.append(int(input()))

for i in range(4):
    lista = []
    for j in range(4):
        lista.append(int(input()))
        if i == j:
            for k in range(n):
                if lista[j] == vet[k]:
                    qtd_igual+=1
        elif i + j == 3:
            veredito = True
            for k in range(n):
                if lista[j] >= vet[k]:
                    veredito = False
            if veredito == True:
                qtd_menores += 1
    mat.append(lista)
    
print('vet:')
for i in range(len(vet)):
    print(vet[i], end=' ')
print('')

print('mat[4][4]:')
for i in range(4):
    for j in range(4):
        print(f'{mat[i][j]}', end=' ')
    print('')

print(f'a)')
print(qtd_igual)
print(f'b)')
print(qtd_menores)
