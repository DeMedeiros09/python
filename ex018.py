import math
n1 = float(input('digite o valor de um ângulo: '))
rad = math.radians(n1)
n2 = math.cos(rad)
n3 = math.sin(rad)
n4 = math.tan(rad)
print('o valor do angulo: {}\nem seno: {:.2f}\nem cosseno: {:.2f}\nem tangente: {:.2f}'.format(n1,n3,n2,n4))
