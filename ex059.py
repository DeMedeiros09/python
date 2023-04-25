print('digite dois valores:\n')
n1 = int(input(('primeiro valor: ')))
n2 = int(input(('segundo valor: ')))

n = int

while n != 5:
  print('-=' * 15)
  print('''o que deseja fazer com esses valores:
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA''')
  n = int(input('digite a opção  desejada: '))
  if n == 1:
    s = n1 + n2
    print('-='* 15)
    print('a soma deu {}'.format(s))
  elif n == 2:
    m = n1 * n2
    print('-=' * 15)
    print('a multiplicação deu {}'.format(m))
  elif n == 3:
    if n1 > n2:
      print('-=' * 15)
      print('o maior é {}\no menor é {}'.format(n1, n2))
    elif n1 < n2:
      print('-=' * 15)
      print('o maior é {}\no menor é {}'.format(n2, n1))
    else:
      print('-=' * 15)
      print('os números são iguais')
  elif n == 4:
    print('-=' * 15)
    n1 = int(input('primeiro número: '))
    n2 = int(input('segundo número: '))
  elif n == 5:
    break
  else:
    print('-=' * 15)
    print('\nescolha uma das opções disponíveis\n')
print('-='* 15)
print('FIM do Programa')
print('-='* 15)