# Solicite a temperatura para o usuário. 
# Se estiver abaixo de 16 graus, informe ao usuário para pegar uma blusa
# Ao final escreva fim do programa

temperatura_ambiente = int(input("Qual é a temperatura ambiente?"))

if temperatura_ambiente <= 16 :
    print()
    print("Pega uma blusa, está frio")
    print("Fim do programa")
    print()

else : 
    print()
    print("Não precisa de blusa")
    print("Fim do programa")
    print()