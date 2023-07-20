vlr_tot = 0
qtd_tot = 0
qtd_atual = 1
while qtd_atual != 0:
    qtd = int(input())
    qtd_atual = qtd
    if qtd > 0 :
        prec_uni = float(input())
        qtd_tot += qtd
        vlr_tot += qtd * prec_uni
print(f'Total: {vlr_tot}')
print(f'Quantidade: {qtd_tot}')
