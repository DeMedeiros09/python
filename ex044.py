p = float(input('digite o preço do produto: '))
print('Digite (1) se for pagar a vista em dinheiro/cheque\nDigite (2) se for pagar a vista no cartão\nDigite (3) se for pagar em duas vezes no cartão\nDigite (4) se for pagar em três vezes ou mais no cartão')
print('-='*27)
fp = int(input('digite o número conforme o tipo de pagamento desejado: '))

if fp == 1:
    d = p * 0.9
    print('o preço do produto agora fica: {}'.format(d))
elif fp == 2:
    d = p * 0.95
    print('o preço do produto agora fica: {}'.format(d))
elif fp == 3:
    print('o preço do produto não irá ser auterado e ficará: {}'.format(p))
elif fp == 4:
    d = p * 1.2
    print('o preço do produto agora fica: {}'.format(d))
else:
    print('Não temos esta opção de pagamento\npor favor digite uma das opções de número acima')