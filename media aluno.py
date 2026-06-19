nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aprovado com média = {media}")

elif media >= 3:
    print(f"Você está de recuperação, sua média foi {media}")
    notarec = float(input("Digite sua nota da recuperação: "))
    if notarec < 6:
        print("Reprovado!")
    else:
        print("Aprovado na recuperação!")

else:
    print(f"Você está reprovado com média = {media}")