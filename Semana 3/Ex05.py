result = 0
menor = 9**9999
operacaoRealizada = False
opcao = int(input())
while opcao != 0:
    operacaoRealizada = True
    if opcao == 1:
        n1 = int(input())
        n2 = int(input())
        result = n1 + n2
        print(f'(a+b) = {result}')
    elif opcao == 2:
        m1 = int(input())
        m2 = int(input())
        m3 = int(input())
        result = m1 + m2 + m3
        print(f'(a+b+c) = {result}')
    elif opcao == 3:
        l1 = int(input())
        l2 = int(input())
        result = l1 * l2
        print(f'(a*b) = {result}')
    else:
        opcao = int(input())
    if result < menor:
        menor = result
    opcao = int(input())
if operacaoRealizada == False:
    print('Nenhum calculo foi realizado!')
else:
    print(f'Menor resultado: {menor}')
