n = int(input())
divisores = 2
if n == 0 or n == 1:
    print('Nao eh Primo!')
else:
    for c in range(2, n):
        if n%c == 0:
            divisores += 1
    if divisores == 2:
        print('Eh Primo!')
    else:
        print('Nao eh Primo!')
