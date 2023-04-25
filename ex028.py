import random
n1 = int(input('adivinhe um número de 1 a 5: '))
Nc = random.randint(1,5)
if n1 == Nc:
    print('Nossa que sorte em... você acertou')
else:
    print('você errou')
print('o número escolhido foi : {}'.format(Nc))