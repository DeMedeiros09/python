import random
p1 = input('escreva o nome de uma pessoa: ')
p2 = input('escreva o nome de uma pessoa: ')
p3 = input('escreva o nome de uma pessoa: ')
p4 = input('escreva o nome de uma pessoa: ')
p5 = input('escreva o nome de uma pessoa: ')
p = [p1,p2,p3,p4,p5]
print('A pessoa escolhida foi : {}'.format(random.choice(p)))

