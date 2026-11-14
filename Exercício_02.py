# Receba ano de nascimento e ano atual. Calcule idade e semanas

# Entrada
Ano_Nascimento = int(input("Digite o seu ano de Nascimento: "))
Ano_Atual = int(input("Digite o ano Atual:"))

# Processamento
Idade = Ano_Atual - Ano_Nascimento
Idade_Semanas = 4 * 12 * Idade

# Saída

print(f"Sua Idade é: {Idade} ")
print()

print(f"Sua Idade em Semanas é: {Idade_Semanas} Semanas")
print()
