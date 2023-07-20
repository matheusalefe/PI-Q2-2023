n = int(input())
soma = 0
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input()))
        if j > i:
            soma += linha[j]

print(f'A soma eh: {soma}')
