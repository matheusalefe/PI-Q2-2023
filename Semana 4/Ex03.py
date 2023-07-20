n = int(input())
e = 0
for c1 in range(1, n+1):
    denom = 1
    for c2 in range (1, c1+1):
        denom = denom*c2
    e += 1/denom
print(f'{e:.1f}')
