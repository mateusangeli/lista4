quantidade = int(input("Digite a quantidade de eleitores: "))

candi1 = 0
candi2 = 0

for eleitor in range(1, quantidade + 1):
  while(True):
    voto = int(input("\nEleitor " + str(eleitor)+ " Digite seu voto. \n [1] João\n [2]Maria \n  "))
    if voto < 1 or voto > 2:
      print("Voto inválido, digite novamente")
    else:
        if voto == 1:
          candi1 += + 1
        else:
          candi2 += 1
        break

print("Candidato 1: %.0i votos " % candi1)
print("Candidato 2: %.0i votos " % candi2)


