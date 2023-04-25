print('-='*20)
n1 = float(input('Digite o valor da casa: '))
print('-='*20)
n2 = float(input('digite seu salário: '))
print('-='*20)
n3 = int(input('digite a quantidade de anos em que irá pagar: '))
n3m = n3 * 12
# o n3m é tempo em meses
n1m = n1 / n3m
n3a = n1 / n3
# o n1m é o valor a se pagar por mês
n2p = n2 * (30/100)
if n1m > n2p:
    print('-' * 40)
    print('\033[;30;107messa casa não poderá ser quitada\033[m\npois a mensalidade da casa por mês da casa ficou {:.2f}, o que excede 30% do seu salário mensal'.format(n1m))
    print('-' * 40)
else:
    print('-'*40)
    print('\033[;97;40messa casa poderá ser quitada\033[m\nVocê pagará {:.2f}R$ por mês, durante {} meses, ou {}R$ por ano, durante {} anos.'.format(n1m,n3m,n3a,n3))
    print('-' * 40)