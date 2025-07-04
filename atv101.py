n = [0,0,0,0]
cont = int(0)
somapar = int(0)
contpar = int(0)

for cont in range (4):
    n[cont] = int(input("Digite um valor. "))

    if(n[cont]%2==0):
        somapar = somapar + n[cont]
        contpar = contpar + 1
    

print(f"São {contpar} números pares e a soma deles é {somapar}. ")