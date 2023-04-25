print('sequencia de Fibonacci')
print('-'*10)
n = int(input('digite a quantida de termos que quer mostrar: '))
c = 2
n1 = 0
n2 = 1
n3 = 0
print('{} -> {}'.format(n1, n2), end=' -> ')
while c < n:
    c += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print('{}'.format(n3), end=' -> ')
print('FIM')