n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 > n2 and n1>n3) or (n1 == n2 and n1 > n3) or (n1 == n3 and n1 > n2):
    print(f'Maior eh: {n1}')
elif n2 > n1 and n2>n3 or (n2 == n1 and n2 > n3) or (n2 == n3 and n2 > n1):
    print(f'Maior eh: {n2}')
elif n3 > n1 and n3>n2 or (n3 == n1 and n3 > n2) or (n3 == n2 and n3 > n1):
    print(f'Maior eh: {n3}')
elif n1 == n2 and n2 == n3:
    print('Numeros Iguais!')
