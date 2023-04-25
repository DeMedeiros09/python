n = int(input('digite um número inteiro: '))
print('escolha uma das bases de conversão abaixo:\n[ 1 ] converter para BINÁRIO\n[ 2 ] coverter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
n1 = int(input('digite a sua opção: '))

if n1 == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif n1 == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)))
elif n1 == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)))
else:
    print('essa obção não existe, ecolha umas das opções acima')