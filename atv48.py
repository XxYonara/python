n1 = int(input("Digite um número."))
n2 = int(input("Digite outro número."))

maior = int(0)
menor = int(999)

if(n1 > maior):
    maior = n1
if(n1 < menor):
    menor = n1
if(n2 > maior):
    maior = n2
if(n2 < menor):
    menor = n2
elif(n1 == n2):
    print("Os números são iguais por isso não existe maior ou menor.")

print("O menor número é "+str(menor)+" e o maior é "+str(maior))
    

