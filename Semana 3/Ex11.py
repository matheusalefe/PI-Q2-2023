qtde_masc = 0
qtde_fem_limitada = 0
qtde_total = 0
media_idade = 0
idade_atual = 1
while idade_atual != 0:
    idade = int(input())
    idade_atual = idade
    if idade != 0:
        sexo = int(input())
        if sexo == 0:
            qtde_masc +=1
        else:
            if idade >= 34 and idade <= 50:
                qtde_fem_limitada += 1
        qtde_total += 1
        media_idade += idade
media_idade = media_idade/qtde_total
print(f'Media: {media_idade}')
print(f'Total Feminino: {qtde_fem_limitada}')
print(f'Total Masculino: {qtde_masc}')
