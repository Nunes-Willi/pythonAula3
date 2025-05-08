
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
numbers = []
count = 0
positives_sum = 0
positives_count = 0


for i in range(20):
    number1 = int(input("valor 1: "))
    numbers.append(number1)

    if numbers[i] < 0:
        print(numbers[i])
    else:
        positives_sum += numbers[i]
        positives_count += 1

if positives_count > 0:
    print(f"Média dos positivos:, {positives_sum / positives_count}" )
else:
    print("Não há números positivos para calcular a média.")