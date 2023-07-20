def obter_valor_funcao(a, b, c):
    d = 1
    soma = 0
    while d <= b:
        soma += c*d
        d += 1
    return a + soma
