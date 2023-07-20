l1 = float(input())
l2 = float(input())
l3 = float(input())

if l1 < (l2 + l3) and l2 < (l3 + l1) and l3 < (l1 + l2):
    print('Eh Triangulo!')
    if l1 == l2 == l3:
        print('Equilatero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isosceles!')
    else:
        print('Escaleno!')
else:
    print('Nao eh Triangulo!')
