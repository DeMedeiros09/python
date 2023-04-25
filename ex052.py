n = int(input('digite um número para ver seus divisores: '))
s1 = 0
s = 0
for c in range(1, n+1):
    if n % c == 0:
        nd = int(n % c == 0)
        s += 1
        s1 += 1
        print('\033[;32m{}\033[m'.format(s), end=' ')
    else:
        s += 1
        print('\033[;31m{}\033[m'.format(s), end=' ')
print('\nO número {} foi divizivel {} veze(s)'.format(n, s1))
if s1 > 2:
    print('E por isso ele não é primo')
else:
    print('E por isso ele é primo')