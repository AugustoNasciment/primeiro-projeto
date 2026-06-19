# Coleta dos dados de peso e altura
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros, ex: 1.75): "))

# Cálculo do IMC utilizando a fórmula indicada na imagem
imc = peso / (altura ** 2)

# Estrutura encadeada para definir o diagnóstico
if imc < 18.5:
    diagnostico = "Abaixo do peso"
elif imc <= 24.9:
    diagnostico = "Peso ideal (parabéns)"
elif imc <= 29.9:
    diagnostico = "Levemente acima do peso"
elif imc <= 34.9:
    diagnostico = "Obesidade Grau I"
else:
    diagnostico = "Obesidade Severa/Mórbida"

# Exibição do resultado
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Diagnóstico: {diagnostico}")