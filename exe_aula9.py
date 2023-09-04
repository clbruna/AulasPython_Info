cadastro_logins = set()
usuarios = list()

print("_"*20, "Menu", "_"*20)
print("""
    Para fazer login digite [1]
    Para se registrar no sistema digite [2]
    Para sair digite [3]
""")
print("_"*46)


while True:

    menu = input("\nSelecione a opção desejada:")

    if menu == "1":

        while True:

            login = input("Digite um nome para login:")

            if login in cadastro_logins != login:
                print("Login já cadsastrado")

            else:
                senha = input("Digite uma senha:")

                usuario = [login, senha]
                usuarios.append(usuario)
                cadastro_logins.add(login)

                resposta = input("Deseja cadastrar um novo login? (sim ou não)").strip()[0].lower()

                if resposta == "n":
                    break

    elif menu == "2":

        print("_" * 40)
        print("Para fazer login digite o usuário e senha.")
        print("_" * 40)

        while True:

            login_entrar = input("Login:")

            if login_entrar in cadastro_logins:

                senha_entrar = input("Digite sua senha:")

                for index in usuarios:

                    if senha_entrar == usuarios[index]:
                        print("Bem vindo!")
                        break

                    else:
                        continue


            else:
                print("Usuário não encontrado")


    else:
        print("_"*40)
        print("Selecione uma das opções!")
        print("_" * 40)

    print(cadastro_logins)
    print(usuarios)
