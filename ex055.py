map = 0
mnp = 0
for c in range(1, 6):
    p = float(input('digite o peso da {}ª pessoa: '.format(c)))

    if c == 1:
        map = p
        mnp = p
    else:
        if p > map:
            map = p
        elif p < mnp:
            mnp = p
print('O maior peso lido é: {}Kg'.format(map))
print('O menor peso lido é: {}Kg'.format(mnp))
