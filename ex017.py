import math
n1 = float(input('digite o valor do primeiro cateto do triangulo retângulo: '))
n2 = float(input('digite o valor do segundo cateto do triangulo retângulo: '))
n3 = math.sqrt((n1**2 + n2**2))
print('o valor do primeiro cateto é: {}\no valor do segundo cateto é: {}\n o valor da hipotenusa é {}'.format(n1,n2,n3))

