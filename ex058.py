import time
import random
nc = random.randint(1, 10)
n = int
c = 0
print('Olá, sou seu computador, pensarei em um número de 1 a 10\nPensando...')
time.sleep(1)
print('Pronto, tente adivinhar')
while n != nc:
    n = int(input('qual seu palpite: '))

    if n > nc:
        print('Menor... tente mais uma vez.')
    elif n < nc:
        print('Maior... tente mais uma vez.')

    c = c + 1
print('\033[;32mVocê acertou com {} tentativas, parabéns\033[m'.format(c))