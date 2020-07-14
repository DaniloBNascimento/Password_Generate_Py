# Pequeno Programa criado para gerar senhas aleatoriamente a partir
#    de uma wordlist de nomes e números.
# Data de criação: 07/07/2020
# Autor: Danilo Bastos
# Data de última alteração: 07/07/2020

# Importando módulos necessários

import random


count = 0

while count == 0:
    print(" ")
    flag = input("Digite 'quit' para sair ou '1' para gerar uma nova senha: ")
    if flag == 'quit':
        exit(0)
    if flag == '1':
        # Definindo uma lista vazia para armazenar nomes
        get_names = []

        # Lendo arquivo para coleta e armazenamento dos nomes
        reading = open('names.txt', 'r')

        # Gravando valores(nomes) em uma lista
        for name in reading:
            get_names.append(name)


        list_exibir = []

        # Gerando números aleatórios
        numbers = random.randint(100, 5000)

        # Lista de caracteres especiais
        carac = ['@', '#', '$', '&', '%', '*']

        printando = random.choice(get_names)
        printando2 = random.choice(carac) + str(numbers)

        exibir = printando + printando2
        list_exibir.append(exibir.replace('\n', ''))

        print(" ")
        print(list_exibir[0].title())

    else:
        print("Digite uma opção válida!")









