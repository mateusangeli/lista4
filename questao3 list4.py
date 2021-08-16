while(True): 
  a = float(input("Digite o valor de A: "))
  if (a == 0):
    print("A equação não é do segundo grau!")
    break
  b = float(input("Digite o valor de B: "))
  c = float(input("Digite o valor de C: "))
  delta = b**2 - 4*a*c
  print("O seu delta foi: ", delta)
  if (delta < 0):
    print("A equação não possui raizes reais")
    break
  if (delta == 0):
    raiz = float(delta) ** 0.5
    x1cima = -b + raiz
    x2cima = -b - raiz
    total1 = x1cima/2*a
    total2 = x2cima/2*a
    print("X1: ", total1)
    print("X2: ", total2)
    print("O valor deu o mesmo para X1 e X2 pois quando delta = 0, só existe 1 raiz real")
    break
  if (delta > 0):
    raiz = float(delta) ** 0.5
    x1cima = -b + raiz
    x2cima = -b - raiz
    total1 = x1cima/2*a
    total2 = x2cima/2*a
    print("X1: ", total1)
    print("X2: ", total2)
    break

