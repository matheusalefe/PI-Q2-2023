x = [0] * 5
y = [0] * 5
li = []

for i in range(0, 5):
    x[i] = int(input())

for j in range(0, 5):
    y[j] = int(input())

for k in range(0,5):
    for l in range(0,5):
        if x[k] == y[l]:
            if len(li) == 0:
                li.append(x[k])
            else:
                contem = False
                for n in range (0, len(li)):
                    if li[n] == x[k]:
                        contem = True
                if contem == False:
                    li.append(x[k])

print(f"O vetor interseccao eh {li}")
