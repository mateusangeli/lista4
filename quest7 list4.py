"""Faça um algoritmo que gera e escreve os 3 primeiros números perfeitos.
Um número perfeito é aquele que é igual a soma dos seus divisores (excluindo ele mesmo).
(Ex.: 6 = l + 2 + 3; 28 = 1 + 2 + 4 + 7 + 14 etc.)"""

n =  int(input("Digite um número: "))
soma = 0
for i in range(1,n):
    print(n, "% ", i, "= ", (n%i))
    if n%i == 0: #não possui resto, logo i é divisível por n
        #print(i)
        soma = soma + i

print("soma: ",soma)
if n == soma:
    print("O número é perfeito!")
else:
    print("Não é perfeito!")