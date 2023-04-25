n = int(input('digite um número [digite 999 para parar]: '))
c = 1
n1 = 0
while n1 != 999:
    c += 1
    n = n + n1
    n1 = int(input('digite outro número [digite 999 para parar] '))
print('foram digitados {} números e a soma deles é {}'.format(c, n))
