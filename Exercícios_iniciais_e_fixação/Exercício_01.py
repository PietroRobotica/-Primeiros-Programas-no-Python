# Receba a idade e anos e imprima em meses, dias, horas e minutos

# Números, textos e booleanos
# Entrada 
idade = int(input("Digite a sua idade: "))
print()

# Processamento 
Idade_Em_Meses = idade * 12
Idade_Em_Dias = idade * 365
Idade_Em_Horas = Idade_Em_Dias * 24
Idade_Em_Minutos = Idade_Em_Horas * 60


print(f"Sua Idade em Meses é: {Idade_Em_Meses} Meses")
print()
print(f"Sua Idade em Dias é: {Idade_Em_Dias} Dias")
print()
print(f"Sua Idade em Horas é: {Idade_Em_Horas} Horas")
print()
print(f"Sua Idade em Minutos é: {Idade_Em_Minutos} Minutos")
