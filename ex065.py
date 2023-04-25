n = float(input('digite um número: '))
c = 1
p = ''
mn = n
mnu = n
s = 0
while p != 'N':
    p = str(input('quer continuar?[S/N]: ').upper())

    if p == 'S' or p == 'Sim' or p == 'SIM':
        n = float(input('digite outro número: '))
        s = n + s
        c = c + 1
        if n > mn:
            mn = n
        elif n < mnu:
            mnu = n
    elif p != 'N':
        print('desculpa não entendemos')
m = s/c



print('Foram digitados {} números\nA média desses números é: {}\nO maior número é {} e o menor é {}'.format(c, m, mn, mnu))