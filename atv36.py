n1 = int(input("Digite um número.")) 
n2 = int(input("Digite um outro número.")) 
n3 = int(input("Digite um outro número."))
n4 = int(input("Digite um outro número."))
par = int(0)
somapar = int(0)
maior = int(0)

if(n1%2==0):
    par += 1
    somapar = somapar + n1
if(n1 > maior):
    maior = n1
if(n2%2==0):
    par += 1
    somapar = somapar + n2
if(n2 > maior):
    maior = n2
if(n3%2==0):
    par += 1
    somapar = somapar + n3
if(n3 > maior):
    maior = n3
if(n1%2==0):
    par += 1
    somapar = somapar + n4
if(n4 > maior):
    maior = n4

print("Foram digitados "+str(par)+" número pares.A soma desses números é "+str(somapar)+" e o maior número é "+str(maior)+".")