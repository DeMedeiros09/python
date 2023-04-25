n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))

m = (n1 + n2) / 2

if m < 5:
    print('\033[;31mREPROVADO')
elif m >= 5 and m < 6.9:
    print('\033[;33mRECUPERAÇÃO')
else:
    print('\033[;32mAPROVADO')