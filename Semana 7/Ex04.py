v_empresa = [0,0]

for k in range(0,2):
    v_empresa[k] = int(input())

n_valores = int(input())
matriz_entregas = [0]*n_valores
v_dist = []

for i in range (0, n_valores):
    matriz_entregas[i] = int(input())

for j in range (1, n_valores, 2):
    v_dist.append(((v_empresa[0] - matriz_entregas[j -1])**2 + (v_empresa[1] - matriz_entregas[j])**2)**(1/2))

for l in range(0, len(matriz_entregas)):
    print(f"{matriz_entregas[l]}", end=' ')
print('')

for m in range(0, len(v_dist)):
    print(f"{v_dist[m]:.2f}", end=' ')
