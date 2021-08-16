numero = int(input("Digite um número: "))
if numero < 1000: 
  c = numero//100
  d = (numero%100)//10
  u = (numero%100)%10
  if c> 0: print("Cs: " if c>1 else "C: ", c)
  if d> 0: print("Ds: "if d>1 else "D: ", d)
  print("Us: "if u>1 else "U: ", u)
else:
  print("Número  maior que mil :(")