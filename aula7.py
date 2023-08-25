
lista = ["rogerio", "pedro", "maria", "joão"]
print(lista)

for index in range(len(lista)):
    lista[index] = lista[index].upper()

print(lista)

print("_"*40)

novaLista = []
novaLista2 = list()
print(type(novaLista))

novaLista.append("Rogerio")
novaLista.append("Carlos")
novaLista.append(1)
novaLista.append(34.56)

print(novaLista)


novaLista2 = []
novaLista2.append("A")
novaLista2.append("D")
novaLista2.append("T")
novaLista2.append("B")
novaLista2.append("C")

print(novaLista2)

print(novaLista2.count("A"))
novaLista2.remove("T")
print(novaLista2)

novaLista2.sort()
print(novaLista2)


