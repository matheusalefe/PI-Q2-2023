qtd = [0] * 6
preco = [0] * 6

for i in range(0, 6):
    qtd[i] = int(input())
    preco[i] = float(input())

faturamento = [0] * 6
media_fat = 0
qtd_fat_mm = 0
for m in range(0, 6):
    faturamento[m] = qtd[m] * preco[m]
    media_fat += (qtd[m] * preco[m]) / 6

for n in range(0, 6):
    if faturamento[n] < media_fat:
        qtd_fat_mm += 1

print('Quantidade:')
for j in range(0, 6):
    print(qtd[j], end=' ')
print('')

print('Preco:')
for k in range(0, 6):
    print(f'{preco[k]:.2f}', end=' ')
print('')

print('Faturamento:')
for l in range(0, 6):
    print(f'{faturamento[l]:.2f}', end=' ')
print('')

print(f'Faturamento Total:{media_fat * 6:.2f}')
print(f'Media dos Faturamentos:{media_fat:.2f}')
print(f'Qtd de Faturamentos Abaixo da Media: {qtd_fat_mm}')
