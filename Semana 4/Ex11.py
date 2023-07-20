n_atual = 1
string = ''

while n_atual != 0:
    n_atual = int(input())
    if n_atual > 0:
        print('POSITIVO')
    elif n_atual < 0:
        print('NEGATIVO')
