# Criar uma lista que vai conter o nome do cliente
# criar uma lista interna que vai ter o contato ( tel, email)
# criar uma lista  interna que tenha 3 notas do cliente
# 1) imprima o nome do cliente
# 2) imprima o somente o telefone  do cliente
# 3) imprimir a soma das notas sum()
# 4) imprimir a contagem do numero das notas len()
# 5) imprimir a a media das notas do cliente junto com o seu nome

cliente1 = ["Carlos", ["(11) 9123-45678", "carlos@gmail"], [10, 8, 7]]

print("Nome:", cliente1[0])
print("Telefone:", cliente1[1][0])
print("Soma das notas:", sum(cliente1[2]))
print("Total de notas:", len(cliente1))
print("Média:", sum(cliente1[2])/len(cliente1[2]))

print(f"\nNome: {cliente1[0]} Média: {sum(cliente1[2])/len(cliente1[2])}")
