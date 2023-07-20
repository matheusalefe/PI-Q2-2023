base = int(input())
expo = int(input())
numero = base
for c in range (1, expo):
    numero *= base
print(numero)
