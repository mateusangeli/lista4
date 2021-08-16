print("Seja bem vindo ao sistema de promoção!, aqui só é permitido comprar 1 tipo de carne por pessoa, porém a quantidade que quiser!")
opc = int(input("Digite [1] para Filé duplo, [2] para Alcatra e [3] para Picanha: "))
while(True):
  if (opc == 1):
    kgF = int(input("Digite quantos kilos de Filé duplo você deseja comprar: "))
    if (kgF <= 5):
      totalf = kgF*4.90
      print("O total da sua compra foi de: %.2f" % totalf)
    else:
      totalf = kgF*5.8
      print("O total da sua compra foi de: %.2f" % totalf)
    forma = int(input("Digite a sua forma de pagamento, sendo [1] para Cartões Tabajara [2] para Cartões normais ou dinheiro: "))
    print("++++ Informações da  compra ++++")
    print("O tipo de carne escolhido  foi Filé duplo e a quantidade foi: ", kgF)
    if (forma == 1):
      desconto = totalf*0.05
      totalc = totalf - desconto
      print("O valor total da compra foi de: %.2f" % totalf)
      print("O desconto feito pelo pagamento no Cartão Tabajara foi: %.2f" % desconto)
      print("O novo preço da compra com o desconto foi de: %.2f" % totalc)
    if (forma == 2):
      print("O valor total da compra foi de: %.2f" % totalf)
    break
  if (opc == 2): 
    kgA = int(input("Digite quantos kilos de Alcatra você deseja comprar: "))
    if (kgA <=5):
      totala = kgA*5.90
      print("O total de  sua compra foi: %.2f" % totala)
    else:
      totala = kgA*6.80
      print("O total da sua compra foi de: %.2f" % totala)
    forma = int(input("Digite a sua forma de pagamento, sendo [1] para Cartões Tabajara [2] para Cartões normais ou dinheiro: "))
    print("++++ Informações da  compra ++++")
    print("O tipo de carne escolhido  foi Alcatra e a quantidade foi: ", kgA)
    if (forma == 1):
      desconto = totala*0.05
      totalc = totala - desconto
      print("O valor total da compra foi de: %.2f" % totala)
      print("O desconto feito pelo pagamento no Cartão Tabajara foi: %.2f" % desconto)
      print("O novo preço da compra com o desconto foi de: %.2f" % totalc)
    if (forma == 2):
      print("O valor total da compra foi de: %.2f" % totala)
    break
  if (opc == 3): 
    kgP = int(input("Digite quantos kilos de Picanha você deseja comprar: "))
    if (kgP <=5):
      totalp = kgP*5.90
      print("O total de  sua compra foi: %.2f" % totalp)
    else:
      totalp = kgP*6.80
      print("O total da sua compra foi de: %.2f" % totalp)
    forma = int(input("Digite a sua forma de pagamento, sendo [1] para Cartões Tabajara [2] para Cartões normais ou dinheiro: "))
    print("++++ Informações da  compra ++++")
    print("O tipo de carne escolhido  foi Picanha e a quantidade foi: ", kgP)
    if (forma == 1):
      desconto = totalp*0.05
      totalc = totalp - desconto
      print("O valor total da compra foi de: %.2f" % totalp)
      print("O desconto feito pelo pagamento no Cartão Tabajara foi: %.2f" % desconto)
      print("O novo preço da compra com o desconto foi de: %.2f" % totalc)
    if (forma == 2):
      print("O valor total da compra foi de: %.2f" % totalp)
    break
    
    