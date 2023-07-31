n = int(input())
while n % 2 != 0:
    print('n deve ser Par!')
    n = int(input())

matriz = []
vogais = ['a','e','i','o','u']
vet = []
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(input())
        veredito = False
        for k in range(5):
            if vogais[k] == lista[j]:
                veredito = True
        if (i+j) == (n-1)  and veredito == True :
            vet.append(lista[j])
    matriz.append(lista)

print('Matriz:')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]}', end=' ')
    print('')

if len(vet) >=1:
    print('Vetor:')
    for i in range(n):
        print(f'{vet[i]}', end=' ')
else:
    print('Nenhuma Vogal!')
