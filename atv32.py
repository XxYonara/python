n1 = int(input("Digite sua idade.")) 
n2 = int(input("Digite sua idade.")) 
n3 = int(input("Digite sua idade.")) 
n4 = int(input("Digite sua idade.")) 
maior = int(0)
menor = int(9999)

if(n1 > maior):
    maior = n1
if(n1 < menor):
    menor = n1
if(n2 > maior):
    maior = n2
if(n2 < menor):
    menor = n2
if(n3 > maior):
    maior = n3
if(n3 < menor):
    menor = n3
if(n4 > maior):
    maior = n4
if(n4 < menor):
    menor = n4


print("O menor é "+str(menor)+" e o maior é "+str(maior))