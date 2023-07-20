x = [0] * 5
y = [0] * 5

for j in range(0, 5):
    x[j] = float(input())

for k in range(0, 5):
    y[k] = float(input())

pe = 0
for i in range(0, 5):
    pe += x[i] * y[i]

print(f"O produto escalar vale {pe}.")
