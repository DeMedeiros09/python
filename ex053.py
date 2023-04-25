p = str(input('digite uma frase ou palavra: ')).upper().strip()

p0 = p.split()
p2 = ''.join(p0)
p1 = ''.join(p0)
pi = p1[::-1]

print('O inverso da palavra {} é {}'.format(p2, pi))

if p2 == pi:
        print('Essa frase ou palavra digitada é um palíndromo')
else:
        print('Essa palavra ou frase digitada não é um palíndromo')