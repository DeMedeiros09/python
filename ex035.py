print('-='*15)
n1 = float(input('primeio lado: '))
print('-='*15)
n2 = float(input('segundo lado: '))
print('-='*15)
n3 = float(input('terceiro lado: '))

if -(n2 - n3) < n1 < n2 + n3:
    if -(n1 - n3) < n2 < n1 + n3:
        if -(n1 - n2) < n3 < n1 + n2:
            print('os seguimentos acima PODEM FORMAR um truiângulo')

else:
    print('os seguimentos acima NÃO FORMAM um triângulo')