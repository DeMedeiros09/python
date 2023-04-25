v = int(input('digite a velocidade de um carro: '))
if v >=81:
    n = v - 80
    x = 7 * n
    print('A sua velocidade foi: {}\nE Você terá de pagar: {}'.format(v,x))
    print('PAGUE O ALUGUEL')
else:
    print('você não pagará nenhuma multa')