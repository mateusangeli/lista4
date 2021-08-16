salario =  1000
ano_inicial = 1995
percent = 1.5
ano_final = 2021
aumento = 0

for ano in range (ano_inicial, ano_final + 1):
  print("Ano: ", ano)
  if ano == 1996:
    aumento = (percent/100)*salario
    
  
  if ano >  1996:
    aumento = (percent/100)*salario
    percent = percent*2

  salario = salario + aumento
  print("\tSalário: R$ %.2f" % salario)
