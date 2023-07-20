sexo = int(input())
altura = float(input())
if sexo == 0:
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print(f'Peso ideal eh: {peso:.2f}')
