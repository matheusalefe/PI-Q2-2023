n = int(input())
v = [0] * n
s = 0
for i in range(0, n):
    v[i] = float(input())
    s += v[i]

m = s/n
nd = 0

for i in range(0, n):
    nd += (v[i] - m) ** 2

dp = (nd/(n-1))**(1/2)
print(f"O desvio padrao vale {dp:.2f}.")
