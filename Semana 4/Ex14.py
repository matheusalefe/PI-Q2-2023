n1 = int(input())
n2 = int(input())
soma_div1 = 0
soma_div2 = 0

for c1 in range (1, n1):
    if n1%c1 == 0:
        soma_div1 +=c1

for c2 in range (1, n2):
    if n2%c2 == 0:
        soma_div2 +=c2

if n1 == soma_div2 and n2 == soma_div1:
    print(f'{n1} e {n2} sao Amigaveis!')
else:
    print(f'{n1} e {n2} NAO sao Amigaveis!')
