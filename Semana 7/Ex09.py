v = [0] * 10
v_switch = [0] * 10
for i in range(0,10):
    v[i] = int(input())

for j in range(0,10):
    if j < 5:
        v_switch[j] = v[j+5]
    else:
        v_switch[j] = v[j-5]

for k in range(0,10):
    print(v_switch[k], end=' ')
