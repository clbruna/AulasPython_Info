#String   toda string é um vetor

#vetor
texto="Rua Floriano de Freitas"

#index     na maioria dar linguagens começa em 0 (0 1 2 3 4 5 6) fatiamento de string

#print(texto[-7]) #se usado numeros negativos o fatiamento é feito ao contrário


#input | processamento ou conversão | output
print(texto.upper())
texto= texto.upper() #deixa todas as letras maiúsculas
print(texto)

texto = texto.lower() #deixa todas as letras minúsculas
print(texto)

#texto = input("Digite seu nome: ")
texto = texto.lower()
print(texto.title()) #tira espaços do início e do final

texto = "    Rogério  sobral"
print(texto.strip())
