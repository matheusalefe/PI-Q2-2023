a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b > c and d > a and (c+d) < (a+b) and a > 0 and c > 0:
    print('Valores aprovados!')
else:
    print('Valores reprovados!')
