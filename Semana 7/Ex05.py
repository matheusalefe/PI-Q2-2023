n = int(input())
while n % 2 == 1:
    print("O n deve ser par!")
    n = int(input())

v = n * [0]
v_inv = n * [0]

for i in range(0, n):
    v[i] = int(input())

for j in range(0, n):
    v_inv[j] = v[n - j - 1]

for k in range(0, n):
    print(v[k], end=' ')
print('')

for l in range(0, n):
    print(v_inv[l], end=' ')
