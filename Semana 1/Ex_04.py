valor_in = float(input(''))
taxa = float(input(''))
tempo = float(input(''))

valor_fi = valor_in*(1+taxa)**tempo

print(f'''Valor = {valor_in}
Taxa de juros = {taxa:.2f}
Tempo = {tempo}
Valor apos o periodo = {valor_fi:.2f}''')
