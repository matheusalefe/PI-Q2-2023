numero = int(input())
ciclo = 1
somador = 1
while ciclo <= numero:
    contador = 1
    while ciclo >= contador:
        print(somador, end=' ')  
        contador += 1
        somador += 1  
    print('\n', end='')
    ciclo += 1
    