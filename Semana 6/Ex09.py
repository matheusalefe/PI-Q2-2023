n1 = int(input())
vet1 = [0] * n1

for i1 in range(0, n1):
    vet1[i1] = int(input())

n2 = int(input())
vet2 = [0] * n2

for i2 in range(0, n2):
    vet2[i2] = int(input())

veredito = True
c = 0
if n1 == n2:
    m_veredito = [False] * n1
    for j in range(0, n1):
        if ((vet1[j] * 2) == vet2[j]) or ((vet2[j] * 2) == vet1[j]):
            m_veredito[j] = True

    while veredito == True and c < n1:
        veredito = m_veredito[c]
        c += 1
else:
    veredito = False

for l in range(0, n1):
    print(vet1[l], end=' ')
print('')

for m in range(0, n2):
    print(vet2[m], end=' ')
print('')
if veredito == True:
    print('Vetor duplicado')
else:
    print('Erro')
