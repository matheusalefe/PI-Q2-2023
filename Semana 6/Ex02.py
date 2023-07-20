soma = 0
v = []
for i in range(5):
    v.append(int(input()))
    soma += v[i]
media = soma/5
for j in range(5):
    print(v[j], end=' ')
print('')
print(f'{media:.2f}')
