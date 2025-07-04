c = int(0)
soma = int(0)

for  cont in range (0,200,1):
    n = int(input("Digite um número."))

    soma = soma + n
    exc =  soma - 1000

    if(soma > 1000):
        print(f"Excedeu em {exc}")
        break

