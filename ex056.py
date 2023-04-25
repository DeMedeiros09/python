so = 0
m = 0
som = 0
sof = 0
mv = 0
nv = ''
for c in range(1, 5):
    print('=' * 5, '{}ª PESSOA'.format(c), '=' * 5)
    n = str(input('NOME: '))
    i = int(input('IDADE: '))
    s = str(input('SEXO [M/F]: ')).strip().upper()
    so = so + i
    m = so / c
    if s == 'M' or s == 'MASCULINO' or s == 'H' or s == 'HOMEM':
        som = som + 1
        if som == 1:
            mv = i
        elif i > mv:
            mv = i
            if mv == i:
                nv = n
    if s == 'F' or s == 'FEMININO' or s == 'MULHER':
        if i < 20:
            sof = sof + 1
print('\nA média de idade do grupo é {}\nO homem mais velho tem {} e o nome dele é {}\nTemos {} mulher(es) com menos de 20 anos'.format(m,mv, nv, sof))
