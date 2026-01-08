# 🧠 DESAFIO 3 — Mini Sistema de Boletim (nível júnior real)
# 🎯 Objetivo

# Criar um mini sistema de boletim escolar usando:

# listas

# dicionários

# funções

# loops

# condicionais

# Nada além do que você já aprendeu + um pequeno empurrão de lógica.

# 📌 Regras do desafio

# ❌ Não usar banco de dados
# ❌ Não usar classes
# ❌ Não usar nada “avançado”

# ✅ Apenas Python básico bem feito

# 🧩 Desafio 3.1 — Estrutura dos dados (primeira parte)

# Você vai cadastrar 3 alunos.

# Cada aluno deve ter:

# nome

# lista de notas

# média

# situação (Aprovado ou Reprovado)

# 👉 Cada aluno deve ser um DICIONÁRIO
# 👉 Todos os alunos devem ficar dentro de uma LISTA

# 🧩 Desafio 3.2 — Função obrigatória

# Você DEVE criar uma função:

# Ela deve:

# receber uma lista de notas

# retornar a média

# ⚠️ Não calcular média fora da função.

# 🧩 Desafio 3.3 — Lógica do programa

# O programa deve:

# 1️⃣ Perguntar o nome do aluno
# 2️⃣ Pedir 3 notas
# 3️⃣ Calcular a média usando a função
# 4️⃣ Definir a situação:
# média >= 7 → Aprovado
# média < 7 → Reprovado
# 5️⃣ Salvar tudo em um dicionário
# 6️⃣ Adicionar o dicionário na lista de alunos
# 7️⃣ Repetir isso para 3 alunos

# 🧩 Desafio 3.4 — Exibição final
# Aluno: Gabriel
# Notas: [8, 7, 9]
# Média: 8.00
# Situação: Aprovado
# ------------------
# Aluno: Maria

# 👉 Use for para percorrer a lista de alunos
# 👉 Use f-string

alunos = []

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    notas = []

    for _ in range(3):
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)

    resultado = calcular_media(notas)

    if resultado >= 7:
        status = "Aprovado!"
    else:
        status = "Reprovado!"

    aluno = {
        "Nome": nome,
        "Notas": notas,
        "Média": resultado,
        "Situação": status,
    }

    alunos.append(aluno)

for aluno in alunos:
    # if aluno["Situação"] == "Aprovado!":
        print(f"""
Aluno = {aluno['Nome']}
Notas = {aluno['Notas']}
Média = {aluno['Média']:.2f}
Situação = {aluno['Situação']}
""")
