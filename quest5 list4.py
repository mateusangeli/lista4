kgm = int(input("Digite quantos quilos de morango você comprou: "))
kga = int(input("Digite quantos quilos de maçã você comprou: "))
kgt = kga+kgm
if (kgm <= 5):
  precom = 2.50
  totalm  = precom*kgm
  print("Morango: %.2f" % totalm)
if (kga <= 5): 
  precoa = 1.80
  totala = precoa*kga
  print("Maçã: %.2f" % totala)
if (kgm > 5):
  precom = 2.20
  totalm = precom*kgm
  print("Morango: %.2f" % totalm)
if(kga > 5):
  precoa = 1.50
  totala = precoa*kga
  print("Maçã: %.2f" % totala)
total = totalm+totala
print("O preço total da compra foi: %.2f" % total)
if (total >= 25 or kgt >= 8):
  totald = total*0.1
  totalf = total - totald
  print("Sua compra com desconto custou: %.2f" % totalf)