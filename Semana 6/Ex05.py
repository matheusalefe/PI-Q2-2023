vet = [0] * 5
soma_pos = 0
cont_neg = 0
existe = False
for i in range(0, 5):
    vet[i] = int(input())

for j in range(0, 5):
    if vet[j] > 0:
        soma_pos += vet[j]
    else:
        cont_neg += 1
print(cont_neg)
print(soma_pos)

num = int(input())
for k in range(0, 5):
    if vet[k] == num:
        existe = True

if existe == True:
    print('Existe!')
else:
    print('Nao existe!')
