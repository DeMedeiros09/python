c = n = s = 0

while True:
    n = int(input('Digite um número (digite 999 para parar): '))
    if n == 999:
        break
    else:
        s += n
        c += 1
print('a soma é dos {} números é {}'.format(c, s))