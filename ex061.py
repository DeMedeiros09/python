print('-='*10)
print('10 termos de uma PA')
print('-='*10)
n = int(input('digite um número: '))
r = int(input('digite a razão dessa PA: '))
s = 1
print('{}'. format(n), end=' -> ')
while s < 10:
    s = s + 1
    n = n + r
    print('{}'.format(n), end=' -> ' if s < 10 else '')
