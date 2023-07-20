def calculo():
    temp_f = float(input())
    temp_c = (5*(temp_f - 32))/9
    return f'{temp_f:.1f}F em C:{temp_c:.1f}'

print(calculo())
