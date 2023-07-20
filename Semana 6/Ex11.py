def inserir():
    vet = 10*[0]
    for i in range (0, 10):
        vet[i] = int(input())
    return vet

def imprimir(vet:list):
    for i in range (0, len(vet)):
        print(f'{vet[i]}', end=' ')
    print('')

def shift(vet:list):
    vet2 = [0] * len(vet)
    for i in range(0, len(vet)):
        if i == 0:
            vet2[0] = vet[len(vet) - 1]
        else:
            vet2[i] = vet[i - 1]
    for j in range(0, len(vet)):
        vet[j] = vet2[j]