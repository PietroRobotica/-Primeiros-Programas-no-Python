# Pense no for como um robô que repete uma tarefa para você para que você não precise digitar a mesma coisa várias vezes.
# Se você tem uma lista de 5 coisas, ele pega a primeira, faz algo com ela, depois pega a segunda, faz de novo, e assim por diante até acabar a lista.

teste = int(input("Digite o numero:"))
intervalo_de_repeticao = int(input("Repetição:"))

for x in range(teste, 100, intervalo_de_repeticao) : # for: Significa "Para..." (indica o início da repetição).
    print(f"x vale: {x}")

# seuquencia é a variável para guardar o item da lista

# O range() é uma ferramenta para gerar sequências de números automaticamente para o for repetir.

# As 3 formas mais usadas são:

# range(fim): Cria números de 0 até um número antes do fim (ex: range(5) gera 0, 1, 2, 3, 4).

# range(inicio, fim): Você escolhe onde começa e onde termina (ex: range(1, 4) gera 1, 2, 3).

# range(inicio, fim, passo): Define início, fim e de quanto em quanto pula (ex: range(0, 6, 2) gera 0, 2, 4).