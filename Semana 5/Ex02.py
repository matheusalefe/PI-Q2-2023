voto = -1
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
brancos = 0
nulos = 0
while voto !=0:
    voto = int(input())
    if voto == 0:
        print(f'''Candidato 1: {candidato_1} voto(s).
Candidato 2: {candidato_2} voto(s).
Candidato 3: {candidato_3} voto(s).

Voto(s) nulo(s): {nulos} voto(s).
Voto(s) branco(s): {brancos} voto(s).\n''')
        if candidato_1 > candidato_2 and candidato_1 > candidato_3:
            print('Candidato vencedor: 1.')
        elif candidato_2 > candidato_1 and candidato_2 > candidato_3:
            print('Candidato vencedor: 2.')
        elif candidato_3 > candidato_1 and candidato_3 > candidato_2:
            print('Candidato vencedor: 3.')
        else:
            print('Empate!')
    elif voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        nulos += 1
    elif voto == 5:
        brancos += 1
    else:
        print('Opcao Invalida!\n')
