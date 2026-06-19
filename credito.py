salario=float(input("Digite o seu salario: "))
parcela=float(input("Digite o valor da parcela: "))
porcentagem=salario*0.3
print(porcentagem)
if parcela>porcentagem:
    print(f" O emprestimo não foi aprovado." )
else:
    print(f" O emprestimo foi aprovado. )")
