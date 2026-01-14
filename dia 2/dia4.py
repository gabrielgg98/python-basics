# 🎯 Objetivo

# A partir da lista alunos (lista de dicionários):

# Média da turma: 7.85

# Melhor aluno:
# - Maria (9.2)

# Pior aluno:
# - João (6.1)

# Aprovados: 2
# Reprovados: 1


# for aluno in alunos:
#     # if aluno["Situação"] == "Aprovado!":
#         print(f"""
# Aluno = {aluno['Nome']}
# Notas = {aluno['Notas']}
# Média = {aluno['Média']:.2f}
# Situação = {aluno['Situação']}
# """)
        


# Calcular:

# Média geral da turma

# Aluno com maior média

# Aluno com menor média

# Quantidade de aprovados e reprovados

# 📌 Regras

# Use funções

# Não use bibliotecas externas

# Não reescreva a lógica de criação dos alunos (reuse o que você já tem)

# Pode criar funções como:

# media_turma(alunos)

# melhor_aluno(alunos)

# pior_aluno(alunos)

# 📥 Estrutura esperada (conceitual)

# Cada aluno é algo assim:

# {
#     "Nome": "Gabriel",
#     "Notas": [7, 8, 9],
#     "Média": 8.0,
#     "Situação": "Aprovado!"
# }

# 📤 Saída esperada (exemplo)
# Média da turma: 7.85

# Melhor aluno:
# - Maria (9.2)

# Pior aluno:
# - João (6.1)

# Aprovados: 2
# Reprovados: 1

# 🧠 Dicas (sem entregar a resposta)

# Você vai precisar:

# somar médias

# comparar valores

# guardar temporariamente “o maior” e “o menor”


turma = []
qtd_notas = 3
media_aprovacao = 7

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    notas = []

    for _ in range(qtd_notas):
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)

    resultado = calcular_media(notas)

    if resultado >= media_aprovacao:
        status = "Aprovado!"
    else:
        status = "Reprovado!"

    aluno = {
        "Nome": nome,
        "Notas": notas,
        "Média": resultado,
        "Situação": status,
    }

    turma.append(aluno)

def media_turma(turma):
    soma = 0

    for aluno in turma:
        soma += aluno['Média']

    media = soma / len(turma)
    return media

turma_media = media_turma(turma) 


def maior_nota(turma):
    max(turma, key=lambda aluno: aluno['Média'])

melhor_aluno = max(turma, key=lambda aluno: aluno["Média"])



def menor_nota(turma):
   max(turma, key=lambda aluno: aluno['Média'])

pior_aluno = min(turma, key=lambda aluno: aluno["Média"])

aprovados = []
reprovados = []

for aluno in turma:
    if aluno["Situação"] == "Aprovado!":
        aprovados.append(aluno["Nome"])

    if aluno["Situação"] == "Reprovado!":
        reprovados.append(aluno["Nome"])


print(f"""
      Média da turma: {turma_media:.2f}
      
      Melhor aluno:
      - Nome: {melhor_aluno["Nome"]}, 
      - Média: {melhor_aluno["Média"]:.2f}

      Pior aluno:
      - Nome: {pior_aluno["Nome"]}, 
      - Média: {pior_aluno["Média"]:.2f}

      Aprovados ({len(aprovados)}): {", ".join(aprovados)} 
      Reprovados ({len(reprovados)}): {", ".join(reprovados)}
      """)
