c = int(0)
impar = int(0)
par = int(0)

while (c != 5):
    c = c + 1
    n = int(input("Digite um número."))
    if(n%2==0):
        par = par + n
    if(n%2==1):
        impar = impar + n

print(f"A soma dos impares é {impar} e a soma dos pares é {par}")