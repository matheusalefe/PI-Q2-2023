p = [0] * 3
q = [0] * 3

for i in range(0, 3):
    p[i] = float(input())
for j in range(0, 3):
    q[j] = float(input())

d = ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2) ** (1 / 2)

print(f"A distancia entre os dois pontos eh {d:.2f}.")
