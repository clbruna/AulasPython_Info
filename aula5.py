#enquanto

#i=0
#while i<=10:
#    print("O valor de i é:", i)
#    i+=1

while True:
    resposta=input("Deseja continuar? sim ou não").strip()[0].lower()

    if resposta=="n":
        break

print("Saiu dosistema")




#idade = input("Digite sua idade:")

#print(idade.isdigit())

#print(idade.isnumeric())

#print(idade.isalpha())

decimal = "12.65"

if str.isdigit(decimal.replace(".", "")):
    decimal = float(decimal)
    print(type(decimal))

else:
    print(type(decimal))