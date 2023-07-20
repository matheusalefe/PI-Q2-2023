ate10 = 0
ate20 = 0
maisDe20 = 0
for c in range(1,11):
    n =int(input())
    if 0 <= n <= 10 :
        ate10 +=1
    elif 11 <= n <= 20 :
        ate20 += 1
    elif 21 <= n :
        maisDe20 +=1

print(f'''>=0 e <=10: {ate10}
>=11 e <=20: {ate20}
>=21: {maisDe20}''')
