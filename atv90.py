c = int(0)
soma = int(0)

while (c != 3):
    c = c + 1
    n = int(input("Digite um número."))

    if(n%2==1 and n%5==0 and n >1 and n < 500):
        soma = soma + n

print(f"A soma é igual a {soma}")
