print('='*30)
print('{:^30}'.format('BANK STEAL YOUR MONEY'))
print('='*30)
cc = 0
cv = 0
cd = 0
cur = 0
v = int(input('qual valor quer sacar: '))
while True:
    if v >= 50:
        v = v - 50
        cc += 1
    if 50 > v >= 20:
        v = v - 20
        cv += 1
    if 20 > v >= 10:
        v = v - 10
        cd += 1
    if 10 > v >= 1:
        v = v - 1
        cur += 1
    if v == 0:
        if cc >= 1:
            print(f'Total de {cc} cédula(s) de R$50')
        if cv >= 1:
            print(f'Total de {cv} cédula(s) de R$20')
        if cd >= 1:
            print(f'Total de {cd} cédula(s) de R$10')
        if cur >= 1:
            print(f'Total de {cur} cédula(s) de R$1')
        break