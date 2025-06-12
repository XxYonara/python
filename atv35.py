resp1 = int(input("Digite um número."))
resp2 = int(input("Digite outro número."))
resp3 = int(input("Digite outro número."))
par = int(0)
impar = int(0)

if(resp1%2==0):
    par = par + resp1
if(resp1%2==1):
    impar = impar + resp1
if(resp2%2==0):
    par = par + resp2
if(resp2%2==1):
    impar = impar + resp2
if(resp3%2==0):
    par = par + resp3
if(resp3%2==1):
    impar = impar + resp3


print("A soma dos números pares é "+str(par)+" e a soma dos impares é "+str(impar)+".")