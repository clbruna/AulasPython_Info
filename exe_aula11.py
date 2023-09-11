# Cadastro de lista de produtos
from datetime import datetime
"""
def produto(tipo, descricao, quantidade):

    tipo = tipo.strip()
    descricao = descricao.strip()
    quantidade = quantidade.strip()

    if len(tipo) != 0 and tipo.isalpha():
        if len(descricao) != 0 and len(descricao) < 100:
            if quantidade.isdigit():
                if int(quantidade) <= 20:

                    return {"tipo": tipo, "descricao": descricao, "quantidade": quantidade}

                else:
                    print("A quantidade deve ser menor que 20.")
            else:
                print("A quantidade deve ser do tipo numérica.")
        else:
            print("A descrição é inválida.")
    else:
        print("O tipo é inválido")



print("Cadastro de produtos".center(30, "_"))

produtos = list()

x = 0

while True:
    tipo = input("Tipo:")
    descricao = input("Descrição:")
    quantidade = input("Quantidade")

    if isinstance(produto(tipo, descricao, quantidade), dict):
        produtos.append(produto(tipo, descricao, quantidade))

    x += 1
    if x == 2:
        break


print(produtos)
"""

def verificarValor (valor):
    if valor.isdigit() or str.isdigit(valor.replace(".", "")) or str.isdigit(valor.replace(",", "")):
        valor = valor.replace(",", ".")
        return float(valor)





def receita (descricao, valor, data, categoria):
    descricao = descricao.strip()
    data = datetime.today()
    categoria = categoria.strip()

    if isinstance(verificarValor(valor), float):
        return {"descricao": descricao, "valor": valor, "data": data, "categoria": categoria}

    else:
        print("Não foi possível cadastrar uma receita")



receitas = list()

while True:
    descricao = input("Descrição:")
    valor = input("Valor:")
    data = datetime.today()
    categoria = input("Categoria:")

    if isinstance(receita(descricao, valor, data, categoria), dict):
        receitas.append(receita(descricao, valor, data, categoria))

    else:
        print("Não foi possivél cadastrar")

    resp = input("Deseja sair? (sim ou não)").strip()[0].lower()

    if resp == "s":
        break


print(receitas)






