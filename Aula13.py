try:
    divisao = 2/1
    lista = [2, 5, 7, 9]
    print(lista[3])

    print(divisao)

except ZeroDivisionError as e:
    print(f"Mensagem de erro: {e}")
except IndexError as e:
    print(f"Outro erro: {e}")
else:
    print("Sem erros")
finally:
    print("Isso sempre sera rodado")
for i in range(10):
    print(i)
