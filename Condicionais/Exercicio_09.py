#  Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a 500 reais.
# Escreva um programa que receba o salário de um funcionário e imprima o valor do salário reajustado 
# ou uma mensagem caso o funcionário não tenha direito a aumento.

nome = input("Digite o seu nome:")
cargo = input("Digite o seu cargo:")
salario = float(input("Digite o seu salario:"))

if salario <= 500 :
    salario_atualizado = (30/100)*salario
    print()
    print(f"{nome}, 30% do seu salário é: R${salario_atualizado}")
    print()
    print(f"Com o acréscimo de 30%, seu salário fica: R${salario_atualizado + salario}")
    print(f"Parabéns {nome}, você teve um aumento de 30% 🔥🔥🔥 ")
    print()

else :
    print()
    print(f"{nome}, infelizmente seu salário não tem direito a aumento😞")
    print()