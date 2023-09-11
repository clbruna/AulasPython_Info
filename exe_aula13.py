# CADASTRO DE PESSOAS (TRABALHANDO COM TRATAMENTO DE ERROS)
# invalid literal for int() with base 10: 'sd'
from datetime import datetime
"""
pessoas = list()

try:
    while True:

        nome = str(input("Nome:"))
        ano_nasc = int(input("Ano de nascimento:"))
        salario = float(input("Salário:"))
        ano_atual = datetime.today()

        print(type(ano_nasc))

        pessoa = (nome, ano_nasc, salario)

        pessoas.append(pessoa)

        resposta = input("Deseja realizar um novo cadstro? (sim ou não)").strip()[0].lower()

        if resposta == "n":
            break




    print(pessoas)

except ValueError as e:
    print("Digite uma idade válida")


# CÁLCULO DE MÉDIA (COM TRATAMENTO DE ERROS)

while True:

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        nota4 = float(input("Nota 4: "))

        notas = (nota1, nota2, nota3, nota4)

        media = sum(notas)/len(notas)

        print(media)

    except ValueError as e:
        print("Digite uma nota válida")
"""

# CÁLCULO DE MÉDIA (COM TRATAMENTO DE ERROS)

while True:

    notas = list()

    try:
        # nota = float(input("Nota: "))
        notas.append(float(input("Nota: ")))
        media = sum(notas)/len(notas)



        resposta = input("Deseja inserir mais notas? (sim ou não)").strip()[0].lower()

        if resposta == "n":
            break

    except ValueError as e:
        print("Digite uma nota válida")

print(media)
