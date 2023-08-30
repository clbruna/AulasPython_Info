# Set
"""
lista = [1 ,2, 3, 4, 2, 3]
tupla = (1, 2, 3, 4, 2, 3)
dicionario = {"um": 1, "dois": 2, "tres": 3}
conjunto = {1, 2, 3, 2, 3}

print(f"lista: {lista}")
print(f"tupla: {tupla}")
print(f"dicionario: {dicionario}")
print(f"conjunto: {conjunto}")

tamanho = len(conjunto)

conjunto.add(4)

if len(conjunto) == tamanho:
    print("Login ja existe.")
"""
logins = {"admin"}
while True:

    login = input("Digite um nome para login:")
    tamanho = len(logins)
    # senha = input("Digite uma senha:")
    logins.add(login)

    if len(logins) != tamanho:
        break

    else:
        print("Esse login já existe.")

    # resposta = input("Deseja cadastrar um novo login? (sim ou não)").strip()[0].lower()

    # if resposta == "n":
        # break