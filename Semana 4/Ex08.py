n = int(input())
prod = 1
if n > 0:
    for c in range(1, n+1):
        prod *= c
    print(f'O fatorial de {n} eh {prod}.')
elif n == 0:
    print(f'O fatorial de {n} eh {prod}.')
else:
    print('Numero inválido!')
