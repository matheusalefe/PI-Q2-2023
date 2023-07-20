n = int(input())
acum_pri = 1
acum_sec = 4
cont_pri = 0
cont_sec = 0
while cont_pri < n:
    cont_sec = 0
    cont_pri += 1
    if cont_pri == n:
        print(acum_pri)
    else:
        print(f'{acum_pri},', end=' ')
        while cont_sec < 2:
            cont_sec += 1
            cont_pri += 1
            if cont_pri == n:
                print(acum_sec)
            else:
                print(f'{acum_sec},', end=' ')
    acum_pri += 1
    acum_sec += 1
