c = 0
pf = 0
pm = 0
pmb = 0
npm = ''
print('''------------------------
    LOJA OLHO DA CARA
------------------------''')
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: '))
    pf = p + pf
    c += 1
    if c == 1:
        pmb = p
    if p < pmb and c > 1:
        pmb = p
        npm = n
    if p > 1000:
        pm += 1


    sn = str(input('quer continuar? [S/N]: ')).upper()
    if sn == 'N':
        break
    elif sn != 'N' and sn != 'S':
        print('Não compreende...')
        sn = str(input('quer continuar? [S/N]: ')).upper()
print('-'*7, 'FIM DO PROGRAMA', '-'*7)
print('\nO total da compra deu: R${:.2f}\nTemos {} produto(os) custando mais de R$1000.00\nO produto mais barato foi {} que custa R${:.2f}'.format(pf, pm, npm, pmb))
