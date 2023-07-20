v = 10 * ['']
v_pares = []
v_impares = []


def verif_dif(num: int, lista: list):
    veredito = True
    for contador in range(0, len(lista)):
        if lista[contador] == num:
            veredito = False
    return veredito


for c in range(0, 10):
    v[c] = int(input())
    if v[c] % 2 == 0 and verif_dif(v[c], v_pares):
        v_pares.append(v[c])
    elif v[c] % 2 == 1 and verif_dif(v[c], v_impares):
        v_impares.append(v[c])

print('Numeros pares:')
if len(v_pares) > 0:
    maior_par = v_pares[0]
    menor_par = v_pares[0]
    for i in range(0, len(v_pares)):
        if v_pares[i] > maior_par:
            maior_par = v_pares[i]
        if v_pares[i] < menor_par:
            menor_par = v_pares[i]

    for k in range(0, len(v_pares)):
        print(v_pares[k])
    print(f'Maior: {maior_par}')
    print(f'Menor: {menor_par}')

print('Numeros impares:')
if len(v_impares) > 0:
    maior_impar = v_impares[0]
    menor_impar = v_impares[0]
    for j in range(0, len(v_impares)):
        if v_impares[j] > maior_impar:
            maior_impar = v_impares[j]
        if v_impares[j] < menor_impar:
            menor_impar = v_impares[j]
    for l in range(0, len(v_impares)):
        print(v_impares[l])
    print(f'Maior: {maior_impar}')
    print(f'Menor: {menor_impar}')
