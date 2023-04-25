n = int(input('digite um número para ver sua tabuada: '))
for c in range(1, 11):
    if c > 0 and c < 11:
        nm = n * c
        print('{} X {} = {}'.format(n, c, nm))
