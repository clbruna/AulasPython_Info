# Sistema de controle

# Versaõ 1

"""
usuarios = list()

while True:

    nome = input("Digit o seu nome:")
    rg = input("Digite seu RG:")
    ano_nasc = input("Digite o ano em que você nasceu:")

    telefones = list()

    tel1 = input("Digite seu primeiro número de telefone:")
    telefones.append(tel1)

    tel2 = input("Digite seu segundo número de telefone:")
    telefones.append(tel2)

    print("Cadastrar despesas:")
    descricao = input("Descrição da despesa:")
    valor = float(input("Valor da despesa:"))

    usuario = {"nome": nome, "RG": rg, "ano": ano_nasc, "telefones": telefones, "despesas": {"descricao": descricao, "valor": valor}}
    usuarios.append(dicionario)

    resposta = input("Deseja continuar? sim ou não").strip()[0].lower()

    if resposta == "n":
        break

print(usuarios)

"""

# Versão 2

import datetime as dt

usuarios = list()

print("Seja bem vindo")

while True:

    print("_"*20, "menu", "_"*20)

    print("""
    Para cadastrar digite [1]
    Para ver todos os usuários digite [2]
    Para sair digite [3]
    """)

    btn = input("Digite a opção desejada:")

    if btn == "1":
        print("_" * 20, "Cadastro de usúario", "_" * 20)

        nome: str = input("Nome:")
        rg: str = input("RG:")
        ano_nasc: str = input("Ano de Nascimento:")


        print("_" * 20, "Cadastro de telefone", "_" * 20)

        tel1: str = input("Didite seu número de telefone:")
        tel2: str = input("Digite um seguando número de telefone:")
        telefones = [tel1, tel2]


        print("_" * 20, "Cadastro de despesa", "_" * 20)

        despesas = list()

        while True:

            descricao: str = input("Descrição da despesa:")
            valor = input("Digite o valor: R$")
            data_despesa = dt.date.today()
            despesa = {"descricao": descricao, "valor": valor, "data_despesa": data_despesa}

            despesas.append(despesa)

            resposta = input("Deseja continuar cadastrando despesas? (sim ou não) ").strip()[0].upper()

            if resposta == "N":
                break

        usuario = {"nome": nome, "rg": rg, "ano_nasc": ano_nasc, "telefones": telefones, "despesas": despesas}
        usuarios.append(usuario)


    elif btn == "2":


        if len(usuarios) <= 0:

            print("Não há usuários cadastrados.")

        else:

            print("_" * 20, "Lista de usuários", "_" * 20)
            for usuario in usuarios:

                print(f'Nome: {usuario["nome"]}')
                print(f'RG {usuario["rg"]}')
                print(f'idade: {dt.date.today().year - int(usuario["ano_nasc"])}')

                print("_" * 20, "Dados de contato", "_" * 20)
                print(f'Tel 1: {usuario["telefones"][0]} | Tel 2: {usuario["telefones"][1]}')

                print("_" * 20, "Despesas", "_" * 20)

                for despesa in usuario["despesas"]:

                    for key, value in despesa.items():

                        if key != "valor":
                            print(f'{key.upper()} = {value}')

                        else:

                            print(f'{key.upper()} = R$ {float(value)}')




    if btn == "3":
        break



















