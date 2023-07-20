qtd_b = 0
qtd_h = 0
qtd_exc = 0
contador = 0
while contador < 5:
    carac = input()
    if carac == 'B':
        qtd_b += 1
    elif carac == 'H':
        qtd_h +=1
    elif carac == '!':
        qtd_exc += 1
    contador +=1
print(f'B: {qtd_b}')
print(f'H: {qtd_h}')
print(f'!: {qtd_exc}')
