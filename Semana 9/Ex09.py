n = int(input())
matriz = []
vet = []
soma = 0
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(int(input()))
        veredito = True
        for k in range(len(vet)):
            if vet[k] == lista[j]:
                veredito = False
        if i >= j and veredito == True:
            vet.append(lista[j])
    matriz.append(lista)

for k in range(len(vet)):
    soma += vet[k]

for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]}', end=' ')
    print('')
print(f'Soma eh: {soma}')