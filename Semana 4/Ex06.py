n = int(input())
adolescentes = 0
sidade = 0
if n <= 2:
    print('Poucos participantes para a pesquisa.')
else:
    for c in range(1, n + 1):
        idade = float(input())
        if 12 <= idade < 18:
            adolescentes += 1
            sidade += idade
    if adolescentes <= 0:
        print('Nenhum adolescente participara da pesquisa.')
    else:
        print(f'A idade media dos {adolescentes} adolescentes é {sidade / adolescentes:.1f} anos.')
