

def mensagem (resposta):
    if resposta == "1":
        print("Você pediu para imprimir.")

    elif resposta == "2":
        print("Você pediu para salvar.")

    elif resposta == "3":
        print("Você pediu para sair.")



# while True:
    # print("""
    # Para imprimeir digitr [1]
    #Para salvar digite [2]
    # Para sair digite [3]
    # """)

    # resposta = input("Qual opção deseja:")
    # mensagem(resposta)
    # if resposta == "3":
    #    break


def pessoa(nome, idade, rg):
    nome = nome.strip()
    idade = idade.strip()
    rg = rg.strip()

    if len(nome) != 0 and nome.isalpha():
        if idade.isdigit() and len(idade) < 3:
            if int(idade) <= 120:
                if len(rg)>=9 and len(rg)<11:

                    return {"nome": nome, "idade": idade, "rg": rg}

                else:
                    print("O valor do RG não é válido")
            else:
                print("A idade deve ser menor do que 120 anos.")
        else:
            print("O valor de idede deve ser numérico.")
    else:
        print("Nome digitado não é válido.")





print("Cadastro de pessoa".center(30, "_"))

x = 0
pessoas = list()


while True:
    nome = input("Digite o seu nome:")
    idade = input("Digite a sua idade:")
    rg = input("Digite o seu RG:")
    if isinstance(pessoa(nome, idade, rg), dict):
        pessoas. append(pessoa(nome, idade, rg))

    x += 1
    if x == 2:
        break


print(pessoas)
