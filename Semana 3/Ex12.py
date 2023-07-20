num_atual = 0
texto = ''
while num_atual >= 0:
    num = int(input())
    num_atual = num
    if num >= 0:
        texto += f'Dobro de {num} eh: {num*2}\n'
print(texto)
