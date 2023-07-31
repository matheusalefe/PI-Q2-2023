def vender_loja(mat:list):
    def soma_linha(matriz:list, linha:int):
        soma = 0
        for i in range(len(matriz[0])):
            soma += matriz[linha][i]
        return soma

    def soma_coluna(matriz:list, coluna:int):
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][coluna]
        return soma

    vet_meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    tot_mes = []
    maior_mes_pos = 0
    maior_mes_valor = 0

    for i in range(12):
        print(f'{vet_meses[i]}: R${soma_linha(mat, i):.2f}.')
        tot_mes.append(soma_linha(mat, i))
        if tot_mes[i] > maior_mes_valor:
            maior_mes_valor = tot_mes[i]
            maior_mes_pos = i

    for i in range(4):
        print(f'Total na semana {i+1} eh: R${soma_coluna(mat, i):.2f}.')

    tot_ano = 0
    for i in range(len(tot_mes)):
        tot_ano += tot_mes[i]

    print(f'Total no Ano: R${tot_ano:.2f}')
    print(f'Mes com Mais Vendas eh: {vet_meses[maior_mes_pos]}.')
