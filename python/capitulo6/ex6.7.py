alunos_notas = {}

quantidade = int(input("Digite a quantidade de alunos: "))

for _ in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos_notas[nome] = nota

alunos_notas_arredondadas = {nome: round(nota) for nome, nota in alunos_notas.items()}

print(alunos_notas_arredondadas)
