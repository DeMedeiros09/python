import math

n = int(input('digite um valor para ver seu fatorial: '))
n1 = math.factorial(n)
print('o fatorial de {} é {}'.format(n, n1))
print('-='*10,'\nsegundo modo:')



n = int(input('digite um valor para ver seu fatorial: '))
c = n
r = 1
print('{}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    r = r * c
    c -= 1
    if c >= 1:
        print('X', end=' ')
    else:
        print('=', end=' ')
print('{}'.format(r), end= ' ')