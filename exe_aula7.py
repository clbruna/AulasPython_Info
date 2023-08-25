import datetime as dt


# 1
nome = ["Rogerio", "Pedro", "carlos"]
print(nome)
nome[1] = "Maria"
print(nome)


# 2
print("_"*50)

print("Seja bem vindo ao sistema")
print("Você precisa logar")

nome:str = input("Digite seu nome:")
senha:str = input("Senha:")

clientes = list()

if nome in ["pedro", "maria", "santos"] and senha == "1234":

    while True:

        print(
                "Para cadastrar clientes digite 1."

              )

        menu = input("Selecone a opção desejada:")

        if menu == 1:

        print("Tela de cadastro")

        nome: str = input("Digite seu nome:")
        rg: str = input("Digite seu RG:")
        cpf: str = input("Digite seu CPF:")
        ano_nasc = int(input("Digite seu ano de nascimento"))

        cliente = [nome, rg, cpf, ano_nasc]

        clientes.append(cliente)

        resposta = input("Deseja realizar um novo cadastro?").strip()[0].upper()

        if resposta == "N":
            break

else:
    print("Nome ou senha não encontrados no sistema")

anoAtual = dt.date.today().year
print(f"Data: {anoAtual}")