# Entrada dos comprimentos das retas
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

# Verificação se as retas podem formar um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print("As retas PODEM formar um triângulo.")

    # Classificação do tipo de triângulo
    if a == b == c:
        print("Tipo: Equilátero (todos os lados iguais)")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles (dois lados iguais)")
    else:
        print("Tipo: Escaleno (todos os lados diferentes)")
else:
    print("As retas NÃO PODEM formar um triângulo.")