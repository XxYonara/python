n1 = int(input("Digite um número."))
n2 = int(input("Digite ouyto número."))
n3 = int(input("Digite outro número."))
par = int(0)
impar = int(0)

if(n1%2==0):
    par +=  1
if(n2%2==0):
    par +=  1 
if(n3%2==0):
    par +=  1
if(n1%2==1):
    impar += 1
if(n2%2==1):
    impar += 1
if(n3%2==1):
    impar += 1

print("Foram encontrados "+str(par)+" números pares e "+str(impar)+"  números impares.")                 
