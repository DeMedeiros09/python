n1 = 0
c = 0

while True:
    n = int(input('escolha um número para ver sua tabuada (digite 0 para terminar): '))
    c = 1
    if n > 0 or n < 0:
        while c <= 10:
            n1 = n * c
            print('{} X {} = {}'.format(n, c, n1))
            c += 1
    else:
        break
print('fim')
