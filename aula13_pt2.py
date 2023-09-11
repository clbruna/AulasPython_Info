
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
    print(arquivoler.read())
