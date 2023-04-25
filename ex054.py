import datetime

at = datetime.date.today().year
s = 0
s2 = 0
n = 0
for c in range(1, 8):

    n = int(input('digite o ano de nascimento da {}ª pessoa: '.format(c)))

    if -n + at >= 18:
        s = s + 1

    else:
        s2 = s2 + 1

print('\n{} são maior de idade'.format(s))
print('{} são menor de idade'.format(s2))
