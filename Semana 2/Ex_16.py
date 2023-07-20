idade = int(input())
if  0 < idade < 18:
    print('Menor de Idade!')
elif 0 < idade >= 18 and idade < 65:
    print('Maior de Idade!')
elif idade >= 65:
    print('Maior de 65 anos!')
else:
    print('Idade Invalida!')
