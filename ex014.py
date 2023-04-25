n1 = float(input('Por quantos dias o carro foi alugado? '))
n2 = float(input('Quantos quilômetros o carro andou? '))
n11 = n1 * 60
n22 = n2 * 0.15
n3 = n22 + n11
print('O carro foi usado por {} dias e rodou {}Km\nO preço a se pagar pelo aluguel do veículo é de {}R$'.format(n1,n2,n3))
