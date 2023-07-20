c = 0
ate2 = 0
maisDe2 = 0
while c <=2:
    pergunta = int(input())
    if pergunta <=2:
        ate2 += 1
    else:
        maisDe2 += 1
    c += 1
print(f'Ate dois filhos: {ate2}')
print(f'Mais de dois filhos: {maisDe2}')
