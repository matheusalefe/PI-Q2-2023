num_atual = 1
lim_x = int(input())
lim_y = int(input())
qtd_limitada = 0
while num_atual != 0:
    n = int(input())
    num_atual = n
    if n != 0:
        if n >= lim_x and n <= lim_y:
            qtd_limitada += 1
print(f'Qtd: {qtd_limitada}')
