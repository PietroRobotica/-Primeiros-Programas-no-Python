# Elabore um programa para cálculo de preços de produtos que solicite o preço de compra do produto e o percentual a ser aplicado em cima desse valor para a venda.
# Calcule e exiba o preço de venda do produto.
# Se o percentual a ser aplicado for inferior a 50%, exiba uma mensagem informando ao usuário que o produto será vendido com uma margem muito pequena de lucro.

preço_produto = float(input("Digite o preço do produto: "))
percentual = float(input("Qual é o percentual de venda?"))
valor_de_Revenda = preço_produto * (percentual/100) + preço_produto


if percentual <= 50 : # Se o desconto for menor que 50%...
    print()
    print(valor_de_Revenda)
    print("O produto tem baixo lucro")
    print()

else :
    print()
    print(valor_de_Revenda)
    print("Lucro bom")
    print()