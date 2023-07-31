def calc_distancia(mat:list, cid_1:int, cid_2:int):
    return f'Distancia entre {cid_1} e {cid_2} eh: {mat[cid_1][cid_2]}'

def total_percorrido(mat:list, vet:list):
    soma = 0
    for i in range(1,len(vet),2):
        soma += mat[vet[i-1]][vet[i]]
    return soma