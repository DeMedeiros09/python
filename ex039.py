a = int(input('digite o ano de seu nascimento: '))
aa = -a + 2023

if aa > 18:
    aaa = aa - 18
    aal = -aaa + 2023
    print('\033[;31mpassou do alistamento\033[m\ndeveri ter se alistado a {} ano(s) atrás, no ano {}'.format(aaa,aal))
elif aa == 18:
    aaa = aa - 18
    aal = -aaa + 2023
    print('\033[;32mhora de se alistar\033[m\nseu alistamento será neste ano de {}'.format(aal))
else:
    aaa = -(aa - 18)
    aal = aaa + 2023
    print('\033[;33mainda vai se alistar\033[m\nirá se alistar da que a {} ano(s), no ano {}'.format(aaa,aal))