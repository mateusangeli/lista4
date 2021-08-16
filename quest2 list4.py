

salario = float(input("Digite o seu salário: "))
if (salario <= 1000):
  salario2 = salario*0.03
  total = salario2+salario
  print("Seu novo salário é: R$ %.2f" % total)
if (salario > 1000 and salario <= 3000):
  salario2 = salario*0.02
  total = salario2+salario
  print("Seu novo salário é: R$ %.2f" % total)
if (salario > 3000 and salario <= 5000):
  salario2 = salario*0.018
  total = salario2+salario
  print("Seu novo salário é: R$ %.2f" % total)