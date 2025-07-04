c = int(1)
p = int(0)
n = int(input("Digite um número."))

if(n <=1 ):
   print("Impossivel")

while (c <= n):
    
    if(n%c==0):
      p = p + 1

    c = c + 1
if(p == 2):
      print("É primo")
else:
    print("Não é primo")
    