n = int(input())
vet = [0] * n

def validar_var(var: int, num: int, nome_var: str):
    while var > (num - 1) or var < 0:
        print(f'Valor de {nome_var} invalido!')
        var = int(input())
    return var

for i in range(0, n):
    vet[i] = int(input())

x = int(input())
x = validar_var(x, n, 'X')

y = int(input())
y = validar_var(y, n, 'Y')

print(f'Soma eh: {vet[x] + vet[y]}')
