salario_atual = 0
soma_salarios = 0
soma_idades = 0
qtd_pessoas = 0
qtd_menos800 = 0

while salario_atual >= 0:
    salario_atual = float(input())
    if salario_atual > 0:
        soma_salarios += salario_atual
        soma_idades += int(input())
        qtd_pessoas += 1
        if salario_atual < 800:
            qtd_menos800 += 1

if qtd_pessoas > 0:
    media_salarios = soma_salarios / qtd_pessoas
    media_idades = soma_idades / qtd_pessoas
    percent_menos800 = qtd_menos800 / qtd_pessoas * 100

    print(f'O salario medio da populacao eh R$ {media_salarios:.2f}.')
    print(f'A idade media eh {media_idades:.2f} anos.')
    print(f'O percentual da populacao com salario menor que R$ 800,00 eh {percent_menos800:.2f}%.')
