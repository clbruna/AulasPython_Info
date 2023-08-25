media = 10
print("Aprovado") if media >= 8 else print("Reprovado")

print("_"*30)

# Aluno 1
nome1 = "Carlos"
idade1 = 45
nota1_aluno_1 = 7
nota2_aluno_1 = 8
nota3_aluno_1 = 9
media_a1 = (nota1_aluno_1 + nota2_aluno_1 + nota3_aluno_1)/3

# Aluno 2
nome2 = "Pedro"
idade2 = 33
nota1_aluno_2 = 9
nota2_aluno_2 = 9
nota3_aluno_2 = 9
media_a2 = (nota1_aluno_2 + nota2_aluno_2 + nota3_aluno_2)/3

print(f"Aluno {nome1} tirou a média de: {media_a1}")
print(f"Aluno {nome2} tirou a média de: {media_a2}")


# Estudo de Listas
# index      0      1   2  3  4
aluno1 = {"Carlos", 45, 7, 8, 9}

print("Nome:",   aluno1[0])
print("idade:",  aluno1[1])
print("Nota 1:", aluno1[2])
print("Nota 2:", aluno1[3])
print("Nota 3:", aluno1[4])

# quero usar somente as notas

media = (aluno1[2] + aluno1[3] + aluno1[4])/3
print(f"Nome {aluno1[0]} tirou a media de: {media}")

# método de listas

print(len(aluno1))

# index 0 1 2 3

