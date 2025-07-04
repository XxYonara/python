cont = int(0)
somapar = int(0)
somaimpar = int(0)
impar = int(0)
par = int(0)
total = int(0)

for cont in range (0,4,1):
    num = int(input("Digite um número."))
    if(num%2==0):
        par = par + 1
    if(num%2==1):
        impar = impar + 1
    if(num%2==0):
        somapar = somapar + num
    if(num%2==1):
        somaimpar = somaimpar + num
    total = somapar + somaimpar

    print(f"Foram cadastrados {par} números pares , e {impar} números impares. A soma dos pares é {somapar},  e a soma impar é {somaimpar} e a soma geral é {total} .")

