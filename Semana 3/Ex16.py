def calcular_pi(n):
    contador = 0
    denom = 1
    sinal = 1
    res = 1
    while contador <= n+1:
        denom += 2
        sinal *= -1
        res += (1/denom) * sinal
        contador +=1
    return res*4
