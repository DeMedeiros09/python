import datetime
ano = int(input('digite o ano de seu nascimento ou digite 0 Se você nasceu esse ano: '))
if ano == 0:
    ano = datetime.date.today().year
id = -ano + 2023
if id <= 9:
    print('\033[;34mMIRIM')
elif id > 9 and id <=14:
    print('\033[;32mINFANTIL')
elif id > 14 and id <= 19:
    print('\033[;31mJUVENIL')
elif id == 20:
    print('\033[;97mSÊNIOR')
elif id > 20:
    print('\033[7;30;107mMASTER\033[m')
