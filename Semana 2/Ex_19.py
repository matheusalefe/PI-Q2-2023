a = int(input())
b = int(input())
c = int(input())

if a == b or a == c or a == b:
    print('Os tres numeros devem ser diferentes!')
elif a < b < c:
    print(a,b,c)
elif a < c < b:
    print(a,c,b)
elif b < a < c:
    print(b,a,c)
elif b < c < a:
    print(b,c,a)
elif c < a < b:
    print(c,a,b)
else:
    print(c,b,a)
