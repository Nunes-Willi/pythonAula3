
#TODO 01
numbers = []
while True:
    try:
        number1 = int(input("valor 1: "))
        numbers.append(number1)
    except ValueError:
        break
    except KeyboardInterrupt:
        break
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

if len(numbers[i]) < 0:
    print("Negativo")
else:
    print(sum(numbers) / len(numbers))


#! Teste de para as varaiáveis
# number1 = int(input("valor 1: "))
# number2 = int(input("valor 2: "))
# number3 = int(input("valor 3: "))
# number4 = int(input("valor 4: "))

# text1 = input("Texto 1: ")
# text2 = input("Texto 2: ")
# text3 = input("Texto 3: ")