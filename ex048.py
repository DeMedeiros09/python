s = 0
co = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            s = s + c
            co = co + 1
            print(c, end=' ')
print('\nA soma de todos {} números é {}'.format(co,s))