A = float(input('digite o número da altura da parede: '))
L = float(input('digite o número da alargura da parede: '))
Q1 = (A * L)//2
Q2 = (A * L)%2
QLT = Q1 + Q2
print('A altura da parede é {}\nA largura da parede é {}\nA área da parede é de {:.3f}m²\n\nA quantidade de baldes de tinta nescessárias para pintar essa parede é {:.3f}'.format(A,L,A*L,QLT))
