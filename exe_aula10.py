import datetime


def calc_idade():
    idade = datetime.date.today().year - int(ano_nasc)
    return idade


ano_nasc = input("Digite o ano em que nasceu:\n")
print(calc_idade())
