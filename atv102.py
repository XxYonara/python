import random 
n = [8,7,6,8]
cont = int(0)
soma = int(0)

for cont in range (0,4,1):
    sort = random.randint(6,8)
    if(n[cont] == sort):
        soma = soma + n[cont]

print(f"{soma}")