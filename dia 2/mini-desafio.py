# Criar lista
# Inserir numeros na lista
# Criar função que retorne a média dos valores
# Exibir média

numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

def num_cal (numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

resultado = num_cal(numeros)

print(resultado)
