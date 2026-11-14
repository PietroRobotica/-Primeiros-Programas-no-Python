# Receba nome, peso e altura. Calcule IMC

# Entrada
nome = input("Digite o seu nome:")
peso = int(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:")) # A variável "Float" é usada para números reais


# Processamento
imc = peso / (altura * altura)


# Saída
print(f"Seu IMC é: {imc}")