N = int(input("Digite o valor de N: "))
m = 1
s = 0
for n in range (1, N +1):
  print(n, "/", m)
  m = m + 2
  s = s + n/m
print("A soma é: ", s)


