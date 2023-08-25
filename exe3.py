# while True:

#    nome = input("Digite seu nome:")
#    idade = int(input("Digite sua idade:"))

#    if idade>18:
#        break

# print("Saiu do sistema")

# ex2

nome = input("Digite o seu nome:")
idade = (input("Digite a sua idade:"))


# só entra no loop se a condição for verdeira
while not (nome.isalpha() and idade.isdigit()):
    print("Você digitou o nome ou a idade incorreta.")

    nome = input("Digite o seu nome novamente:")
    idade = (input("Digite a sua idade novamente:"))


while True:

    # bamdeiras
    b1 = False
    b2 = False
    b3 = False
    b4 = False

    nota1 = input("Digite sua primeira nota:")

    if str.isdigit(nota1.replace(".", "")) or str.isdigit(nota1.replace(",", "")):
        nota1 = float(nota1.replace(",", "."))
        print("depois ", nota1)
        b1 = True

    else:
        print("Você digitou a primeira nota errada")
        b1 = False

    nota2 = input("Digite sua sugunda nota:")

    if str.isdigit(nota2.replace(".", "")) or str.isdigit(nota2.replace(",", "")):
        nota2 = float(nota2.replace(",", "."))
        print("depois ", nota2)
        b2 = True

    else:
        print("Você digitou a segunda nota errada")
        b2 = False

    nota3 = input("Digite sua terceira nota:")

    if str.isdigit(nota3.replace(".", "")) or str.isdigit(nota3.replace(",", "")):
        nota3 = float(nota3.replace(",", "."))
        print("depois ", nota3)
        b3 = True

    else:
        print("Você digitou a terceira nota errada")
        b3 = False

    nota4 = input("Digite sua quarta nota:")

    if str.isdigit(nota4.replace(".", "")) or str.isdigit(nota4.replace(",", "")):
        nota4 = float(nota4.replace(",", "."))
        print("depois ", nota4)
        b4 = True

    else:
        print("Você digitou a quarta nota errada")
        b4 = False

    if b1 and b2 and b3 and b4:
        media = (nota1 + nota2 + nota3 + nota4) / 4
        print("Média:", media)
        break

print("aprovado")
