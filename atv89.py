c = int(0)
par = int(0)
somapar = int(0)

for cont in range(0,6,1):
    n = int(input("Digite um número."))

    if(n%2==0):
        par = par + 1
        somapar = somapar + n

print(f"Foram digitados {par} números pares e a soma entre eles é {somapar}.")