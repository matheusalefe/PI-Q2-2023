numero = int(input())
while numero < 0:
    print('O numero deve ser >=0!')
    numero = int(input())
while numero >= 0:
    print(numero, end=' ')
    numero -=1
print('\nFIM!')
