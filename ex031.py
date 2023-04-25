n = float(input('digite a distância de sua viagem em quilômetros: '))

if n <= 200:
    n1 = n * 0.5
    print('O preço de sua viagem ficou: {}'.format(n1))

else:
    n1 = n * 0.45
    print('O preço de sua viagem ficou: {}'.format(n1))
