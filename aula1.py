# Aula 1 Variáveis

frase = "Hello Word!"

nome = "Bruna"
sobrenome = "Morais"  #strint = texto
peso = 70.800   #floate = real
idade = 23

endereco = "Rua Floriano de Freitas"
cpf = "xxx.xxx.xxx-xx"
ddd = "11"
telefone = "xxxx-xxxxx"




#print(type(idade))  #print= =saída de dados no terminal | typ = função que mostra o tipo primitivo

print("Nome:", nome, "\nSobrenome:", sobrenome, "\nIdade:", idade, "\n\nEndereço:",
      endereco, "\nCPF:", cpf, "\nTelefone:", ddd, telefone, "\n\n\n\n" )

print("#"*50)

print(f"Nome: {nome} \nSobrenome: {sobrenome} \nIdade: {idade}")

print("#"*50)

#rg=input("Digite seu RG:")   #todo valor do input vem como string
#idade=int(input("Digite sua idade:"))

#Operadores Math
# + = soma
# - = subtração
# / = divisão
# // = divisão inteira
# % = módulo (entrega o resto da divisão)
# * = multiplicação
# ** = potenciação

print("#"*50)

#nota1 = float(input("Digite a primeira nota:"))
#nota2 = float(input("Digite a segunda nota:"))
#nota3 = float(input("Digite a terceira nota:"))
#nota4 = float(input("Digite a quarta nota:"))

#print("Média:", (nota1 + nota2 + nota3 + nota4) / 4)

print("#"*50)

nome = input("Digite seu nome:")
rg = input("Digite seu RG:")
cpf = input("Digite seu CPF:")

print(f"\n\nSeu nome é: {nome} \nSeu RG é: {rg} \nSeu CPF é: {cpf}")

