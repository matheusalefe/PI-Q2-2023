A = [0]*5
B = [0]*5
C = [0]*5

for i in range(0, 5):
    A[i] = int(input())
    C[i] += A[i]

for j in range(0,5):
    B[j] = int(input())
    C[j] -= B[j]

for k in range(0,5):
    print(C[k], end=' ')
