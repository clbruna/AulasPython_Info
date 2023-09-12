"""
try:
    arquivo = open("texto.txt", "x")

except FileExistsError as e:
    print("O arquivo já existe")


texto = input("Digite algo:")

try:
    arquivo = open("texto.txt", "a")
    arquivo.write(texto)

except:
    pass

try:
    arquivoler = open("texto.txt", "r")

except Exception as e:
    print("Valor:", e)
finally:
    print(arquivoler.read())"""

def criarArquivoPessoas():
    try:
        arquivo = open("pessoas.txt", "+r")
        arquivo.close()
        return True

    except Exception as e:
        print("Não fou possível criar o arquivo")
        return False



def addPessoa(nome, rg, ano_nasc):
    pessoa = f'"Nome:"{nome}, "rg:"{rg}, "ano:"{ano_nasc}\n'
    try:
        arquivo = open("pessoas.txt", "   a")
        arquivo.write(pessoa)
        arquivo.close()

    except Exception as e:
        print("Não foi possível adicionar essa pessoa", e)



def listaPessoas():
    try:
        arquivo = open("pessoas.txt", "r")
        texto = arquivo.readlines()
        arquivo.close()
        return texto

    except Exception as e:
        print("Não foi possível ler o arquivo pessoas, Erro", e)



# CRIANDO O SISTEMA

valor = criarArquivoPessoas()

while True:

    if valor:
        print("MENU".center(40, "#"))

        print("""
        OPÇÃO 1 -> CADASTRAR
        OPÇÃO 2 -> LISTAR
        OPÇÃO 3 -> SAIR
        """)

        pergunta = input("Qual opção deseja?")

        if pergunta == "1":
            print("CADASTRAR".center(40, "#"))

            nome = input("Nome:")
            rg = input("RG:")

            try:
                ano = input("Ano de nascimento:")
                addPessoa(nome=nome, rg=rg, ano=ano)
            except Exception as e:
                print("Digite um ano válido\n Erro: ", e)

        elif pergunta == "2":
            texto = listaPessoas()
            print(texto)

        elif pergunta == "3":
            break

        else:
            print("Digite uma das opções.")


