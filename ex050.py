s = 0
co = 0
for c in range(1, 7):
    n = int(input('digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s = s + n
        co = co + 1
print('a soma dos {} números pares é: {}'.format(co, s))

