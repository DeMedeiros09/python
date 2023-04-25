n1 = float(input('digite um número: '))
n2 = float(input('digite outro número: '))
n3 = float(input('digite outro número: '))

if n1 == n2 and n1 == n3 and n2 == n3:
    print('os números são iguais')
else:
    if n1 >= n2 and n1 >= n3:
        print('o número {} é o maior'.format(n1))
    else:
        if n2 >= n1 and n2 >= n3:
            print('o número {} é o maior'.format(n2))
        else:
            if n3 >= n1 and n3 >= n2:
                print('o número {} é o maior'.format(n3))
if n1 == n2 and n1 == n3 and n2 == n3:
    print('os números são iguais')
else:
    if n1 <= n2 and n1 <= n3:
        print('o número {} é o menor'.format(n1))
    else:
        if n2 <= n1 and n2 <= n3:
            print('o número {} é o menor'.format(n2))
        else:
            if n3 <= n1 and n3 <= n2:
                print('o número {} é o menor'.forat(n3))