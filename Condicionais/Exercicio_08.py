# Faça um programa que receba o nome, cargo e salário de um funcionário. 
# Se o funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. 
# Ao final exiba o nome, o cargo e o salário desse funcionário.

nome = input("Digite o seu nome:")
cargo = input("Digite o seu cargo:")
salario = float(input("Digite o seu salario:"))

if salario <= 1000 :
    salario_atualizado = (10/100)*salario
    print()
    print(f"{nome}, 10% do seu salário é: {salario_atualizado}")
    print()
    print(f"Com o acréscimo de 10%, seu salário fica: {salario_atualizado + salario}")



    
