a = int(input("Digite um número."))
b = int(input("Digite um outro número."))
c = int(input("Digite um outro número."))

maoir = int(0)
menor = int(0)
meio = int(999)

if(a > b and a > c and b > c):
    maior = a
    meio = b
    menor = c
if(a > b and a > c and c > b):
    maior = a
    meio = c
    menor = b
if(b > a and b > c and a > c):
    maior = b
    meio = a
    menor = c
if(b > a and b > c and c > a):
    maior = b
    meio = c
    menor = a
if(c > a and c > b and a > b):
    maior = c
    meio = a
    menor = b
if(c > a and c > b and b > a):
    maior = c
    meio = b
    menor = a

print("O maior é "+str(maior)+" o do meio é "+str(meio)+" e o menor é "+str(menor))
