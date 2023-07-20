v_original = [0]*6
v_correto = [0]*6

for c in range(0, 6):
    v_original[c] = int(input(''))

for i in range (5, -1, -1):
    v_correto[(i - 5) * -1] = v_original[i]

for j in range(0,6):
    print(v_correto[j], end=' ')
