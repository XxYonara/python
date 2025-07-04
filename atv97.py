nt = [0,0,0,0,0,0]
media = int(0)
maior = int(0)
menor = int(999)
soma = int(0)
cont = int(0)

for cont in range(6):
    nt[cont] = int(input("Digite a sua  nota."))
    soma = soma + nt[cont]
    media = soma / 6


    if(nt[cont] > maior ):
        maior = nt[cont]
    if(nt[cont] < menor):
        menor = nt[cont]

print(f"A média é {media} e a maior  nota é {maior} e a menor é {menor} ")