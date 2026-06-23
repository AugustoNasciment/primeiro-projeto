
ano_atual = 2026
maiores = 0
menores = 0

for i in range(7):
    ano = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    idade = ano_atual - ano

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Maiores de idade: {maiores}")
print(f"Menores de idade: {menores}")
