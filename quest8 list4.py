maior_salario = 0
menor_salario = 99999


while(True):


  nome  = input("Digite  o nome do funcionário: ")
  salario  = float(input("Digite o salário: "))

  if(salario >= maior_salario):
    maior_salario = salario
    print("Maior salario: R$ %.2f" % maior_salario)
  if(salario <= menor_salario):
    menor_salario = salario
    print("Mmenor salario: R$ %.2f" % menor_salario)
    


  
  sair = input("Digite 's' para sair: ")
  if sair == "s":
    break

print("Maior salario: R$ %.2f" % maior_salario)
print("Menor salario: R$ %.2f" % menor_salario)

