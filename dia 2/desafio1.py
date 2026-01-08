# 📌 Enunciado
# Crie um programa que:

# 1) Peça ao usuário:

# nome (string)

# idade (int)

# salário (float)

# 2) Com base no salário, classifique a pessoa:

# até 3000 → "Júnior"

# de 3000.01 até 6000 → "Pleno"

# acima de 6000 → "Sênior"

# 3) Com base na idade:

# se idade >= 18, status = "Maior de idade"

# se idade < 18, status = "Menor de idade"

# 5) Ao final, exiba uma única mensagem, por exemplo:

# Nome: João
# Idade: 25 (Maior de idade)
# Salário: 4500.0
# Nível: Pleno

# 📐 Regras

# Não use funções ainda

# Não use listas nem dicionários

# Use apenas:

# variáveis

# if / elif / else

# operadores

# input / print


nome = input("Digite aqui o seu nome: ")


idade = int(input("Digite aqui a sua idade: "))

if idade >= 18:
    status = "Maior de idade"
else:
    status = "Menor de idade"


salario = float(input("Digite aqui o seu salário: "))

if salario <= 3000:
    nivel = "Júnior"
elif 3000 < salario <= 6000:
    nivel = "Pleno"
else:
    nivel = "Sênior"


mensagem = f"""
Nome: {nome}
Idade: {idade} ({status})
Salário: R$ {salario: .2f}
Nível: {nivel}
"""

print(mensagem)