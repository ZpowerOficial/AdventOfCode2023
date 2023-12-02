import re
# Lê o documento de calibração como uma lista de linhas
documento = open("entradasdia1.txt").read().splitlines()
documento = [linha.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine") for linha in documento]
# Inicializa a soma dos valores de calibração como zero
soma = 0

# Para cada linha no documento
for linha in documento:
    # Inicializa o primeiro e o último número como vazios
    primeiro = ""
    ultimo = ""
    # Para cada caractere na linha
    for caractere in linha:
        # Se o caractere é um dígito
        if caractere.isdigit():
            # Se o primeiro número ainda não foi encontrado
            if primeiro == "":
                # Atribui o caractere ao primeiro número
                primeiro = caractere
            # Atualiza o último número com o caractere
            ultimo = caractere
    # Combina os dois números para formar um número de dois dígitos
    valor = int(primeiro + ultimo)
    # Adiciona o valor à soma
    soma += valor

# Imprime a soma dos valores de calibração
print(soma)
