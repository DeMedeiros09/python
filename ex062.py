import time
print('GERADOR DE PA')
print('-='*10)

n = int(input('digite o primeiro número da PA: '))
r = int(input('digite a razão da PA: '))
s = 1
npa = 10
c = 1
print('{}'.format(n), end=' -> ')
while s < npa:
    c += 1
    s = s + 1
    n = n + r
    print('{}'.format(n), end=' -> ' if s < npa else '\nPAUSA...')
    if s == npa:
        time.sleep(0.5)
        npa = int(input('\nquantos termos da PA você quer mostrarar a mais (digite 0 para encerrar): '))
        if npa > 0:
            s = 0
        elif npa == 0:
            print('FIM')
            break
print('A PA foi finalizada com {} termos mostrados'.format(c))


