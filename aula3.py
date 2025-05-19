import math
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
# x = 1.0

# while x <= 5.0:
#     y = (3 + 2*x + 6*x**2) / (1 + 9*x + 16*x**2)
#     print(f"x = {x:.1f} -> y = {y:.4f}")
#     x += 0.1
#     x = round(x, 1)

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
# n = int(input("Digite o valor de N: "))
# s = 0

# for i in range(1, n + 1):
#     s += i / (n - i + 1)

# print(f"Valor de s: {s:.2f}")

#TODO 14
# s = 0
# sign = 1

# for i in range(1, 102, 2):
#     s += sign * (1 / (i**3))
#     sign *= -1

# pi_aprox = (s * 32) ** (1/3)

# print(f"Valor aproximado de pi: {pi_aprox:.2f}")

#TODO 15
# soma = 0
# numerador = 100

# for i in range(20):
#     termo = numerador / math.factorial(i)
#     soma += termo
#     numerador -= 1

# print(f"Soma dos 20 termos: {soma:.2f}")

#TODO 16
# x = float(input("Digite o valor de x: "))
# soma = 0

# for i in range(30):
#     termo = (x ** i) / math.factorial(i)
#     soma += termo

# print(f"Valor aproximado de e^{x} = {soma:.2f}")

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

# # print("\nLucro máximo: R${:.2f}".format(lucro_max))
# # print("Melhor preço: R${:.2f}".format(melhor_preco))
# # print("Ingressos: {}".format(melhor_ingressos))

#TODO 19
# n = int(input("Quantos números você quer testar?: "))

# for _ in range(n):
#     numero = int(input("Digite um número inteiro: "))
#     divisores = []

#     for i in range(1, numero + 1):
#         if numero % i == 0:
#             divisores.append(i)

#     print(f"Número lido = {numero}; \n Divisores = {divisores}; \n Quantidade de divisores = {len(divisores)}\n")

#TODO 20
# cookieByHour = 1
# cookieBroken = 0
# for hora in range(16):
#      cookieBroken += cookieByHour
#      cookieBroken *= 3

# print(f"Total de biscoitos quebrados em 16 horas: {cookieBroken}")

#TODO 21
# alunos_18 = []
# contador_maior_20 = 0

# for i in range(5):
#     nome = input(f"Digite o nome do aluno: ")
#     idade = int(input(f"Digite a idade de {nome}: "))

#     if idade == 18:
#         alunos_18.append(nome)
#     if idade > 20:
#         contador_maior_20 += 1

# print("\nAlunos com 18 anos:")
# for aluno in alunos_18:
#     print(aluno)

# print(f"\nQuantidade de alunos com mais de 20 anos: {contador_maior_20}")

#TODO 22
# n = int(input("Qauntia de pessoas: "))
# somaMulheres = 0
# contMulheres = 0
# somaTotal = 0

# for _ in range(n):
#     altura = float(input("Altura (em metros): "))
#     sexo = input("Sexo (M/F): ").strip().upper()

#     somaTotal += altura

#     if sexo == 'F':
#         somaMulheres += altura
#         contMulheres += 1

# media_mulheres = somaMulheres / contMulheres if contMulheres > 0 else 0
# media_total = somaTotal / n

# print(f"Média de altura das mulheres: {media_mulheres:.2f} m")
# print(f"Média de altura da turma: {media_total:.2f} m")

#TODO 23
# while True:
#     nome = input("Nome do cliente: ")
#     if nome.upper() == "ULTIMO":
#         break

#     endereco = input("Endereço do cliente: ")
#     valor = float(input("Valor da compra: R$ "))

#     if valor > 500:
#         total = valor * 0.80
#     else:
#         total = valor * 0.85

#     print(f"Total a pagar (cliente {nome}): R$ {total:.2f}")

#TODO 24
# somaIdades = 0
# contIdades = 0

# while True:
#     idade = int(input("Digite a idade: "))
#     if idade > 0:
#         somaIdades += idade
#         contIdades += 1

#     opcao = input("Deseja digitar mais um valor? (s/n): ").strip().lower()
#     if opcao != 's':
#         break

# if contIdades > 0:
#     media = somaIdades / contIdades
#     print(f"Idade média do grupo: {media:.2f} anos")
# else:
#     print("Nenhuma idade válida foi digitada.")

#TODO 25
# diarias = int(input("Número de diárias: "))
# valorDiaria = 50.00

# if diarias < 15:
#     taxa = 7.50
# elif diarias == 15:
#     taxa = 6.50
# else:
#     taxa = 5.00

# total = diarias * (valorDiaria + taxa)
# print(f"Total a pagar: R$ {total:.2f}")