n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))

if n1 == n2:
    print('não existe valor maior ou menor\n\033[;30;107mos dois números são iguais\033[m')
if n1 > n2:
    print('\n\033[;30;107mo número {} é o maior\033[m'.format(n1))
elif n2 > n1:
    print('\n\033[;30;107mo número {} é o maior\033[m'.format(n2))
if n1 < n2:
        print('\n\033[;30;107mo número {} é o menor\033[m'.format(n1))
elif n2 < n1:
        print('\n\033[;30;107mo número {} é o menor\033[m'.format(n2))
