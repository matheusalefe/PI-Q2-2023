num_atual = 1
soma_mult_3 = 0
qtd_mult_3 = 0
while num_atual > 0:
    num = int(input())
    num_atual = num
    if num > 0:
        if num % 3 == 0:
            soma_mult_3 += num
            qtd_mult_3 += 1
if qtd_mult_3 == 0:
    qtd_mult_3 = 1
print(f'Media eh: {soma_mult_3/qtd_mult_3}')
