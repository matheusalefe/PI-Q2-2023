numero = int(input())
contador = 0
while contador <= numero:
    print(f'{contador} ', end='')
    contador += 1
print('\n', end='')
while contador >= 1:
    print(f'{contador-1} ', end='')
    contador -= 1