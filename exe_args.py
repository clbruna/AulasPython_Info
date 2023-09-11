from datetime import datetime

def verificarValor (valor):
    if valor.isdigit() or str.isdigit(valor.replace(".", "")) or str.isdigit(valor.replace(",", "")):
        valor = valor.replace(",", ".")
        return float(valor)



def receita (descricao, valor, data, categoria):
    descricao = descricao.strip()
    data = datetime.today()
    categoria = categoria.strip()

    if isinstance(verificarValor(valor), float):
        return [descricao, valor, data, categoria]

    else:
        print("Não foi possível cadastrar uma receita")



def organizador(*args):
    descricao = args[0]
    valor = args[1]
    data = args[2]
    categoria = args[3]

    print(f"DESCRIÇÃO: {descricao}")
    print(f"VALOR: {valor}")
    print(f"DATA: {data}")
    print(f"CATEGORIA: {categoria}")






receitas = list()

while True:
    descricao = input("Descrição:")
    valor = input("Valor:")
    data = datetime.today()
    categoria = input("Categoria:")

    if isinstance(receita(descricao, valor, data, categoria), list):
        receitas.append(receita(descricao, valor, data, categoria))

    else:
        print("Não foi possivél cadastrar")

    resp = input("Deseja sair? (sim ou não)").strip()[0].lower()

    if resp == "s":
        break


print(receitas)

organizador(descricao, valor, data, categoria)

