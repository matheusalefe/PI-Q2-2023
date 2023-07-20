n = int(input())
v = [0] * n
for i in range(0, n):
    v[i] = int(input())

vo = [0] * n

for j in range(0, n):
    c = 0
    for k in range(0, n):
        if v[j] <= v[k]:
            c += 1
    vo[n - c] = v[j]

for m in range(0, n):
    if vo[m] == 0 and m != 0:
        vo[m] = vo[m - 1]

for l in range(0, n):
    print(vo[l], end=' ')
