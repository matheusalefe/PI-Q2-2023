n = int(input())
while n % 2 == 0:
    print("O n deve ser impar!")
    n = int(input())

v = n * [0]
v_inv = n * [0]

for i in range(0, n):
    v[i] = int(input())

for j in range(0, n):
    if j == n // 2:
        v_inv[j] = 'X'
    else:
        v_inv[j] = v[n - j - 1]

for k in range(0, n):
    print(v[k], end=' ')
print('')

for l in range(0, n):
    print(v_inv[l], end=' ')
