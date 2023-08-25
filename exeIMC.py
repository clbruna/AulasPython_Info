peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

imc = peso/(altura**2)

if imc < 16:
    print(f"Magreza grave")

elif imc >= 16 and imc < 17:
    print(f"Magreza moderada")

elif imc >=17 and imc < 18.5:
    print("Magreza leve")

elif imc >= 18.5 and imc < 25:
    print("Saudável")

elif imc >= 25 and imc < 30:
    print("Sobrepeso")

elif imc >=30 and imc < 35:
    print("Obesidade Grau 1")

elif imc >= 35 and imc < 40:
        print("Obesidade Grau 2")

else:
    print("Obesidade Grau 3")
