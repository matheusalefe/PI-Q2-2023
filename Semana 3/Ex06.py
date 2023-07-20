numero = int(input())
contador = 1
soma = 0
while contador < numero:
    if numero % contador == 0:
        soma += contador
    contador += 1
print(soma)
