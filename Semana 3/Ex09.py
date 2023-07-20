limite = int(input())
contador = 0
pot = 0
while pot < limite:
    pot = 2 ** contador
    if pot*2 < limite:
        print(pot, end=', ')
    elif pot < limite:
        print(pot)
    contador += 1
