import random
adv = random.randint(0, 100)
chute = int(input("Adivinha (0 à 100): "))

while chute != adv:
    if chute < adv:
        print("Maior")
        chute = int(input("Adivinha (0 à 100): "))
    else:print("Menor")
    chute = int(input("Adivinha (0 à 100): "))
    # print("Errooouuuu")
    # chute = int(input("Adivinha (0 à 100): "))

print("Acertou")