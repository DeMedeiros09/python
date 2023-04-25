s = ''
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo [M/F]: ')).upper()
    if s != 'M' or s != 'F':
        print('Dados invalidos, por favor informe seu sexo')

print('Sexo {} registrado com sucesso'.format(s))