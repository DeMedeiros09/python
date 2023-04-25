import random
p1 = input('digite um nome de uma pessoa: ')
p2 = input('digite um nome de uma pessoa: ')
p3 = input('digite um nome de uma pessoa: ')
p4 = input('digite um nome de uma pessoa: ')
p = [p1,p2,p3,p4]
random.shuffle(p)
print('A sequencia será: {}'.format(p))