x = int(input())
y = int(input())
if x > 2 and y > 2:
    for c in range(1, x + 1):
        if c == 1 or c == x:
            print('+' * x)
        else:
            print('+', ' ' * (x - 2), '+', sep='')
else:
    print('Dimensoes fora das especificacoes.')
