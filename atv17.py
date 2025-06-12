num = int(input("Digite um valor."))
num2 = int(input("Digite outro valor"))
num3 = int(input("Digite outro valor"))

cont = int(0)

if(num > 25):
    cont += 1
if(num2 > 25):
    cont += 1
if(num3 > 25):
    cont += 1

print("Encontramos "+str(cont)+" números maior do que 25")   