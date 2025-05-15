
#TODO 01
#? WHILE
# numbers = []
# count = 0
# while count < 20:
#     try:
#         number1 = int(input("valor 1: "))
#         numbers.append(number1)
#     except ValueError:
#         break
#     except KeyboardInterrupt:
#         break
#     count += 1

# i = 0
# positives_sum = 0
# positives_count = 0

# while i < len(numbers):
#     if numbers[i] < 0:
#         print(numbers[i])
#     else:
#         positives_sum += numbers[i]
#         positives_count += 1

#     i += 1

# if positives_count > 0:
#     print("Média dos positivos:", positives_sum / positives_count)
# else:
#     print("Não há números positivos para calcular a média.")

#? FOR
# numbers = []

# for i in range(20):
#     try:
#         number1 = int(input("valor 1: "))
#         numbers.append(number1)
#     except ValueError:
#         print("O item colocado não é um número")
#         break
#     except KeyboardInterrupt:
#         print("Programa encerrado")
#         break

# positives_sum = 0
# positives_count = 0

# negatives_exist = False
# for num in numbers:
#     if num < 0:
#         print(num)
#         negatives_exist = True
#     else:
#         positives_sum += num
#         positives_count += 1

# if not negatives_exist:
#     print("Não há números negativos.")

# if positives_count > 0:
#     print(f"Média dos positivos: {positives_sum / positives_count}")
# else:
#     print("Não há números positivos para calcular a média.")

#TODO 02
# count = 0

# while count < 15:
#     try:
#         number = int(input("Coloque um número inteiro: "))
#         if number % 2 == 0:
#             print(f"O {number} é par")
#         else:
#             print (f"O {number} é ímpar")
#         count += 1
#     except ValueError:
#         print("Valor colocado não é um número inteiro")
#         break
#     except KeyboardInterrupt:
#         print("Programa encerrado")
#         break

#TODO 03
# menor = None
# maior = None
# while True:
#     try:
#         numero = int(input("Digite um número: "))
#         if numero == 0:
#             break
#         elif numero < 0:
#             print("Por favor, digite um número inteiro positivo.")
#             continue
#         elif menor is None or numero < menor:
#             menor = numero
#         elif maior is None or numero > maior:
#             maior = numero

#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")
#         break

# if menor is None:
#     print("Nenhum número válido foi digitado.")
# else:
#     print(f"O menor número digitado foi: {menor}")
#     print(f"O maior número digitado foi: {maior}")

#TODO 04
# par = 0
# impar = 0
# for n in range(1, 101):
#     if n % 2 == 0:
#         par += n
#     else: impar += n

# print(f"Soma dos pares {par}")
# print(f"Soma dos ímpares {impar}")

#TODO 05
# altura = []
# for i in range(20):
#     try:
#         alto = float(input("Coloque uma altura em cm: "))
#         if alto < 300:
#             altura.append(alto)
#         else:
#             print("Calma lá titan")
#             break
#     except ValueError:
#         print("Erro de valor")
#         break
#     except KeyboardInterrupt:
#         print("Programa encerrado")
#         break

# print(f"{sum(altura) / len(altura):.2f}")

#TODO 06
# n = int(input("Quantia de vezes do loop: "))
# contador_negativos = 0

# for i in range(n):
#     numeros = int(input("Valores: "))
#     if numeros < 0:
#         contador_negativos += 1
#     else: print("Não há numeros negativos")

# print(f"Quantidade de valores negativos: {contador_negativos}")

#TODO 07
# tinta = float(input("Quantia de tinta em %: "))

# if 1 >= tinta <= 100:
#     while tinta > 0.001:
#         tinta = tinta - ((2 / 100) * tinta)
#         if tinta >= 0.001:
#             print(f"Enquanto tem tinta a caneta escreve (qtd de tinta restante {tinta:.2f})")
#         else:
#             print("Acabou a tinta")
# else: print("O valor min. é 1 e max. é 100%")

#TODO 08
# atletas = []
# qtd = int(input("Quantia de atletas: "))
# for n in range(qtd):
#     insc = int(input("Inscrição do atleta: "))
#     altura = int(input("Altura do atleta em cm: "))
#     atletas.append((insc, altura))

# if 80 < altura < 300 or insc == 0:
#     mais_alto = max (atletas, key=lambda x: x[1])
#     print(f"\n Incrição do atleta: {mais_alto[0]}, Mais alto: {mais_alto[1]} cm")

#     mais_baixo = min(atletas, key=lambda x: x[1])
#     print(f"\n Inscrição: {mais_baixo[0]}, Mais baixo: {mais_baixo[1]} cm")

#     print(f"\n Média das alturas: {sum(altura for _, altura in atletas) / len(atletas)}")
# else:
#     print("\n Tem algo de errado \n altura min é 80cm, max 300cm e incrição != 0")

#TODO 09



#TODO 10
# fatorial = int(input("Escreva um numero para fatorar: "))

# for i in range(1, n + 1):
#     fatorial *= i

# print(f"O fatorial de {n} é {fatorial}")

#TODO 11
# somar = 0
# for n in range(1, 101):
#     somar += n

# print(somar)

#TODO 12
# somar = 0
# for n in range(1, 101):
#     somar += 1 / n

# print(round(somar, 2))

#TODO 13

#TODO 14

#TODO 15

#TODO 16

#TODO 17
# audiencia = {4: 0, 5: 0, 9: 0, 12: 0}
# total = 0

# n = int(input("Quantidade de casas: "))

# for _ in range(n):
#     canal = int(input("Canal (0 se desligado): "))
#     pessoas = int(input("Pessoas assistindo: "))

#     if canal in audiencia and pessoas > 0:
#         audiencia[canal] += pessoas
#         total += pessoas

# print("\nAudiência por canal:")
# if total == 0:
#     print("Nenhuma TV ligada.")
# else:
#     for canal in sorted(audiencia):
#         percentual = (audiencia[canal] / total) * 100
#         print(f"Canal {canal}: {percentual:.2f}%")

#TODO 18
# lucro_max = 0
# melhor_preco = 0
# melhor_ingressos = 0

# for i in range(9):
#     preco = 5.0 - (i * 0.5)
#     ingressos = 120 + (i * 26)
#     lucro = (preco * ingressos) - 200

#     print(f"R${preco:.2f}  | {ingressos:^9} | R${lucro:.2f}")

#     if lucro > lucro_max:
#         lucro_max = lucro
#         melhor_preco = preco
#         melhor_ingressos = ingressos

# print("\nLucro máximo: R${:.2f}".format(lucro_max))
# print("Melhor preço: R${:.2f}".format(melhor_preco))
# print("Ingressos: {}".format(melhor_ingressos))

#TODO 19
n = int(input("Quantia de loops: "))
divisores = []
for x in range(n):
    try:
        if n < 1 or not int:
            print("Não pode")
    except ValueError:
        break
    else:
        number = int(input("Coloque um numero Int: "))
        for i in range(2, number + 1):
            if (number % i == 0):
                divisores.append(i)
                print(f"Os numero {number} tem {len(divisores)} divisores, sendo {divisores}")