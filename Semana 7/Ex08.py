n = int(input())
while n < 4:
    print('N invalido!')
    n = int(input())

v = [0] * n
for i in range(0, n):
    v[i] = int(input())

menores = [0, 0, 0]

for j in range(-1, n - 1):
    contador = 0
    for k in range(-1, n - 1):
        if v[j + 1] <= v[k + 1]:
            contador += 1
    if contador == n:
        menores[0] = v[j + 1]
    elif contador == n - 1:
        menores[1] = v[j + 1]
    elif contador == n - 2:
        menores[2] = v[j + 1]

for l in range(0, 3):
    print(menores[l], end=' ')
