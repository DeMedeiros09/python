import random
c = 0
while True:
    a = random.randint(0, 10)

    n = int(input('Digite um número: '))
    mpi = str(input('Você quer Par[P] ou Impar[I]: ')).upper()
    pi = n + a
    print(f'Você jogou {n} e o computador jogou {a} dando {pi}')
    pi = pi % 2

    if mpi == 'P':
        if pi == 0:
            print('\033[;32mVocê acertou, Deu Par\033[m')
            c += 1
        else:
            print('\033[;31mtu errou mano')
            if c == 0:
                print('\nVocê não venceu nenhuma partida')
                break
            else:
                print(f'\n\033[;34mvocê venceu um total de {c} partidas consecutivas')
                break
    elif mpi == 'I':
        if pi != 0:
            print('\033[;32mVocê acertou, Deu Impar\033[m')
            c += 1
        else:
            print('\n\033[;31mTu errou mano')
            if c == 0:
                print('\nVocê não venceu nenhuma partida')
                break
            else:
                print(f'\n\033[;34mvocê venceu um total de {c} partidas consecutivas')
                break
            