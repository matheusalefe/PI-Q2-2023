n = int(input())
numerador = 1
denominador = 1
soma = 0
for c in range (1, n+1):
    soma += numerador/denominador
    numerador += 1
    denominador += 2
print(f'{soma:.2f}')
