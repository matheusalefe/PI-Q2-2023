qtd_requerida = int(input())
numero_de_primos = 0
string = ''
numero_atual = 2
while numero_de_primos < qtd_requerida:
    divisores = 2
    for c in range(2, numero_atual+1):
        if numero_atual%c == 0 and c != numero_atual :
            divisores += 1
    if divisores == 2:
        numero_de_primos += 1
        string += f'{numero_atual} '
    numero_atual += 1
print(f'{qtd_requerida} numero(s) primo(s):')
print(string)
