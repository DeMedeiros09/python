import time
import random

print('VAMOS JOGAR JOKENPÔ')
print('digite (1) para jogar \033[;30;107mPEDRA\033[m\ndigite (2) para jogar \033[;97mpapel\033[m\ndigite (3) para '
      'jogar \033[;34mtesoura\033[m')
print('-=' * 23)
n1 = int(input('digite uma das opções acima conforme quer jogar: '))

n2 = random.randint(1, 3)

print('JÓ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')

if n1 == 1 and n2 == 2:
    print('\n\033[;31mVOCÊ PERDEU!!!\033[m\nvocê escolheu \033[;30;107mPEDRA\033[m\no computador escolheu \033[;97mPAPEL')
elif n1 == 1 and n2 == 3:
    print('\n\033[;32mVOCÊ VENCEU!!!\033[m\nvocê escolheu \033[;30;107mPEDRA\033[m\no computador escolheu \033[;34mTESOURA')
elif n1 == 2 and n2 == 1:
    print('\n\033[;32mVOCÊ VENCEU!!!\033[m\nvocê escolheu \033[;97mPAPEL\033[m\no computador escolheu \033[;30;107mPEDRA\033[m')
elif n1 == 2 and n2 == 3:
    print('\n\033[;31mVOCÊ PERDEU!!!\033[m\nvocê escolheu \033[;97mPAPEL\033[m\no computador escolheu \033[;34mTESOURA')
elif n1 == 3 and n2 == 1:
    print('\n\033[;31mVOCÊ PERDEU!!!\033[m\nvocê escolheu \033[;34mTESOURA\033[m\no computador escolheu \033[30;107mPEDRA\033[m')
elif n1 == 3 and n2 == 2:
    print('\n\033[;32mVOCÊ VENCEU!!!\033[m\nvocê escolheu \033[;34mTESOURA\033[m\no computador escolheu \033[;97mPAPEL')
elif n1 == n2:
    print('\n\033[;97;40mDEU EMPATE....\033[m')
else:
    print(
        '\n\033[;31messa opção não existe\033[m,você não sabe jogar jokenpô não, burrão de mais... escolha umas das '
        'opções acima')
