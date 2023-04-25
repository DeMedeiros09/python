s = str(input('digite a palavra (homem) se você é homem ou digite a palavra (mulher) se você é mulher: '))
p = float(input('digite o seu peso ek kg: '))
ac = int(input('digite a sua altura em centímetros: '))
i = int(input('digite a sua idade: '))

s = s.strip()
s1 = s.lower()
if s1.count('o') == 1:
    gc = 66 + (13.7 * p) + (5 * ac) - (6.8 * i)
    print('o seu gasto de caloria basal por dia é: {}'.format(gc))
elif s1.count('l') == 1:
    gc = 665 + (9.6 * p) + (1.8 * ac) - (4.7 * i)
    print('o seu gasto de caloria basal por dia é: {}'.format(gc))
