# 🎯 Objetivo

# Criar um pequeno sistema que:

# Receba notas de alunos

# Armazene os dados

# Calcule média

# Informe aprovação ou reprovação

# Tudo no terminal, sem banco de dados, do jeito certo pra consolidar fundamentos.

# 📌 Regras do desafio

# Você deve:

# Criar uma função chamada calcular_media(notas)

# A função deve:

# Receber uma lista de notas

# Retornar a média


# No programa principal:

# Pedir o nome do aluno

# Pedir 3 notas (usando for)

# Armazenar as notas em uma lista

# Após calcular a média:

# Se média ≥ 7 → Aprovado

# Se média < 7 → Reprovado

# Exibir no final:

# Nome

# Notas

# Média (formatada com 2 casas decimais)

# Situação

# 🧠 Regras pedagógicas

# ❌ Não usar nada que você ainda não viu (ex: classes)

# ✅ Pode usar f-string

# ❌ Não usar bibliotecas externas

# ✅ Código legível > código curto


nome = input("Digite seu nome: ")

notas = []

for _ in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media

resultado = calcular_media(notas)

if resultado >= 7:
    status = "Aprovado!"
else:
    status = "Reprovado!"

mensagem = f"""
Nome = {nome}
Notas = {notas}
Média = {resultado:.2f}
Situação = {status}
"""
print(mensagem)