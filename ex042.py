a = float(input('digite o tamanho do primeiro lado do triangulo: '))
b = float(input('digite o tamanho do segundo lado do triangulo: '))
c = float(input('digite o tamanho do terceiro lado do triangulo: '))

# FORMULA PARA FAZER UM TRIÂNGULO:
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a == b == c:
        print('O triângulo é \033[;32mEQUILÁTERO')
    elif a == b != c or c == a != b or b == c != a:
        print('o triãngulo é \033[;30mISOSCELES')
    elif a != b and a != c and b != c:
        print('o triângulo é \033[;34mESCALENO')
else:
    print('\033[;31mESSES LADOS NÃO FORMAM UM TRIÂNGULO')
