import random

velocidade =  random.randint(0, 100)

print(f"velocidade do carro: {velocidade} km/h")

if velocidade > 80:
    print(f"Você foi multado! A sua velocidade de: {velocidade} km/h ultrapassou o limite de 80 km/h.")
else:
    print(f"Boa viagem, dirija com segurança!")

