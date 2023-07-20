n = int(input())
vet = [0] * n
for j in range(0, n):
    vet[j] = int(input())

for k in range(0, n):
    print(vet[k], end=' ')
print('')
i = int(input())

for l in range(0, n):
    if l >= i and l < n - 1:
        vet[l] = vet[l + 1]
    elif l == n - 1:
        vet[l] = -1

for m in range(0, n):
    print(vet[m], end=' ')
