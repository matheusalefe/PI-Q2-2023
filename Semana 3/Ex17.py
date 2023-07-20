def qtd_digitos_impares(n):
    impares = 0
    copia = n
    while copia != 0:
        if copia % 2 !=0:
            impares +=1
        copia = int(copia/10)
    return impares
