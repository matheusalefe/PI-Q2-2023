n_atual = int(input())
maior = n_atual
menor = n_atual
if n_atual != -5:
    while n_atual != -5:
        n_atual = int(input())
        if n_atual != -5:
            if maior < n_atual:
                maior = n_atual
            if menor > n_atual:
                menor = n_atual
print(f'Maior: {maior}')
print(f'Menor: {menor}')
