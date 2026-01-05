# "main" é uma boa prática em python, representando o arquivo principal para rodar algum script



# [EXERCÍCIO] 

print ("Quero meu primeiro emprego!")

# "print" é uma forma de exibir alguma informação no terminal



# Varáveis servem para armazenar dados, sejam textos, números positivos e negativos e decimais
# Booleana armazena valores de "true" e "false"
# String são textos
# INT são números inteiros
# FLOAT são números decimais

# [EXERCÍCIO]
nome = input("Digite seu nome:")
idade = int( input("Digite sua idade:"))
peso = float( input("Digite seu peso:"))

print(nome)
print(type(idade))
print(type(peso))

# "input" nos permite ler entrada de dados do usuário // Retorna os valores como STRING, em certos momentos 
# será necessário realizar a conversão (ou cast)



# OPERADORES realizam operações matemáticas dentro de variáveis

# [EXERCÍCIO]
soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("soma", soma)
print("multiplicação", multiplicacao)
print("divisão", divisao)
print("potência", potencia)



# CONDICIONAIS são mudanças de fluxo do programa baseado em determinadas condições pré-estabelecidas
# "if" = "se" // "else" = "se não" // "elif / else if" = "ou então"

# [EXERCÍCIO]

idade = int( input("Informe a sua idade:"))

if idade >= 18:
    print("PERMITIDO!")
else:
    print("ACESSO NEGADO!")
# Esse espaço (identação) de texto entre a linha de cima e a de baixo, representa que a inferior é uma instrução dentro do código
# = 1 tab ou 4 espaços

# [EXERCÍCIO]

salario = float( input("Informe o seu salário:"))

if salario <= 3000:
    print ("Programador Junior")
elif salario > 3000 and salario < 6000:
    print ("Programador Pleno")
elif salario > 6000 and salario < 15000:
    print ("Programador Sênior")
else:
    print("Gerente de Projetos")



# LISTAS são um conjunto de dados armazenados em uma variável
# Listas possuem indíce (index), sempre começando no 0; 0, 1, 2...
#Listas podem ter strings, ints e floats
# .append é um método para incluir um dado à uma lista vazia - Existem diversos outros métodos, pesquisar no google sobre
# len() = quantidade de dados na lista
# min() = exibe o menor valor
# max() = exibe o maior valor

# [EXERCÍCIO]

lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])



# REPETIÇÕES servem para executar um bloco de instrução repetidamente
# FOR = repetição com número de repetição definidas
# WHILE = repete instruções com repetições definidas ou eternamente

# [EXERCÍCIO]

for x in range(5):  O "x" é uma variável temporária que será modificada de acordo com a execução do loop. x=0, x=1, x=2...

notas = []

for x in range (2):
    codigo_aluno = input ("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print( "quantidade de notas", len(notas) )

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota: ", nota)

# [EXERCÍCIO]

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input ("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1

print( "quantidade de notas", len(notas) )

for n in notas: 
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota: ", nota)


# OBS: não entendi muito bem o conceito de while e for nesse exercício em questão, preciso revisar!



# DICIONÁRIOS (ou objetos) são estruturas que armazenam informações utilizando chaves e valor
# variavel = {
# "chave": "valor",
# }
# Essa função permite incluir diversas informações (atributos) dentro de uma mesma variável

# import os # no python é possível importar scripts do python ou de outras pessoas

# [EXERCÍCIO]

mensagens = []

nome = input("Nome: ")


while True:

    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_______________")

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })

# FUNÇÕES são blocos reutilizáveis de código que realizam tarefas específicas, sem precisar ficar replicando o código diversas vezes, apenas chamando a função


# [EXERCÍCIO]
def minha_funcao (valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor 1: "))
    if valor1 == 00:
        break
    valor2 = int(input("Valor 2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)

    
# A partir de agora entre todos os dias no GPT e peça desafios com dificuldade progressiva, para aprender, errar e continuar evoluindo