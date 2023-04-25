ci = 0
cm = 0
cf = 0
c = 0
while True:
    print('''-----------------------
  CADASTRE UMA PESSOA
-----------------------''')
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    c += 1
    if i > 18:
        ci += 1
    if i < 20 and s == 'F':
        cf += 1
    if s == 'M' or s == 'm':
        cm += 1
    sn = str(input('Quer continuar? [S/N]: ')).upper()
    if sn == 'N':
        break
print('\nAo todo temos {} pessoa(s) cadastrada(s)\nO total de pessoas com mais de 18 anos é: {}\nAo todo temos {} homem(ns) cadastrado(s)\nTemos {} mulher(es) cadastrada(s) com menos de 20 anos de idade'.format(c, ci, cm, cf))

