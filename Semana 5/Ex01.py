# Variável de escolha do usuário
# (a) = Área do triângulo
# (b) = Área do círculo
# (c) = Área do trapézio
opcao = input()

if opcao == 'a' or opcao == 'A':
    base = float(input())
    altura = float(input())
    print(f'Area do triangulo eh: {(base*altura)/2:.2f}.')
elif opcao == 'b' or opcao == 'B':
    raio = float(input())
    print(f'Area do circulo eh: {3.14*(raio**2):.2f}.')
elif opcao == 'c' or opcao == 'C':
    base_m = float(input())
    base_M = float(input())
    altura = float(input())
    print(f'Area do trapezio eh: {(base_m + base_M)*altura/2:.2f}.')
else:
    print('Opcao Invalida!!')
