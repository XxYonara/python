n = [0,0,0,0]
cont = int(0)
somapar = int(0)
somaimp = int(0)

for cont in range (4):
    n[cont] = int(input("Digite um valor. "))

    if(n[cont]%2==0):
        somapar = somapar + n[cont]
    if(n[cont]%2==1):
        somaimp = somaimp + 1

print(f"A soma dos pares é {somapar} ,e são {somaimp} números impares.")