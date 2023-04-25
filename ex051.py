s = 0
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n1 = float(input('digite o primeiro termo da PA: '))
n2 = float(input('digite a razão da PA: '))

print('{:.0f}'.format(n1),end=' -> ')
for c in range(1, 10):
    s = s + n2
    n3 = s + n1
    print('{:.0f}'.format(n3),end=' -> ')
print('FIM DA PA')