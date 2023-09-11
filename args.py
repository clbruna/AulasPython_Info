# Calculadora
"""
def calculadora(*args):

    operador: str
    valor1: str
    valor2: str

    for index, parametro in enumerate(args):
        if index == 0:
            operador = parametro

        elif index == 1:
            valor1 = parametro

        elif index == 2:
            valor2 = parametro

        print(f"Operador: {operador}")
        print(f"Valor 1: {valor1}")
        print(f"Valor 2: {valor2}")



calculadora("+", 34, 5)
"""

# Função args kargs


# vou entrar com a possibilidade de varios parametros, e não quero limitar minha função com uma
#quantidade de parametros
def calculadora(*args):

    operador: str
    valor1: str
    valor2: str

    for index, parametro in enumerate(args):

        if index == 0:
            operador = parametro

        elif index == 1:
            valor1 = parametro

        elif index == 2:
            valor2 = parametro

    print(f"Qual operador é : {operador}")
    print(f"Qual  é o valor 1 : {valor1}")
    print(f"Qual  é o valor 2 : {valor2}")

#index        0  1  2   3
calculadora("+", 34, 5)
