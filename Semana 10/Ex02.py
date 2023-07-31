n = int(input())
while n % 2 != 0 or n < 4:
    print('n deve ser par e >=4!')
    n = int(input())

lista = [0] * n
x = 0
for i in range(n):
    if i < n/2:
        lista[i] = int(input())
    else:
        lista[(n-1) - x] =int(input())
        x += 1

for i in range(n):
        print(f'{lista[i]}', end=' ')
