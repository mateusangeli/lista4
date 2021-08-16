horas_cliente = float(input("Digite a quantidade de horas que ficou no estacionamento: "))
valor = 0
if horas_cliente <=3:
  valor = 4
else: 
    #caso horas maior que 24
    if(horas_cliente >=24):
      h24_co =  horas_cliente//24 # periodos que se passaram 24h
      h24_res = horas_cliente%24 # quantidade de horas restantes
      print("h24_co: ", h24_co)
      print("h24_res: ", h24_res)
      valor += h24_co*31.0 +4

      horas_cliente = h24_res
  
  
    h_corrente = horas_cliente//3 
    h_restante = horas_cliente%3 
    print("h_corrente: ",h_corrente)
    print("h_restante: ",h_restante)

    valor = valor + h_corrente*4.00
    valor  = valor + h_restante*1.5
    if h_restante  < 3:

print("Valor a ser pago: R$ %.2f" % valor)

    





