#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite aqui o seu primeiro nome: ")
salario = float(input("Qual o seu salário atual? "))
bonus = float(input("Qual o multiplicador da PLR no ano de 2024? "))

plr = 1000.00 + (salario * bonus)

print(f"Parabéns {nome}, a sua PSL será de R${plr} reais!")