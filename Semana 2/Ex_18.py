n1 = float(input())
n2 = float(input())
opcao = int(input())

if opcao > 4 or opcao <= 0:
    print('Opcao Invalida!')
elif opcao == 4 and n2 == 0:
    print('N2 nao eh diferente de zero!')
elif opcao == 1:
    media = (n1 + n2)/2
    print(media)
elif opcao == 2:
    if n1 > n2:
        dif = n1 - n2
    else:
        dif = n2 - n1
    print(dif)
elif opcao == 3:
    prod = n1*n2
    print(prod)
else:
    razao = n1/n2
    print(razao)
