c= int(0)

resto = int(0)

while (c != 1):
    c = c + 1
    n = int(input("Qual valor desejar sacar ?"))

   
    nt50 = int(n / 50)
    resto = (n - (nt50 * 50))
    nt20 = int(resto / 20)
    resto = (resto - (nt20 * 20))
    nt10 = int(resto / 10)
    resto = (resto -(nt10 * 10))
    nt2 = int(resto / 2)
    resto = (resto - (nt2 * 2))
    nt1 = int(resto / 1)
    resto = (resto -(nt1 * 1))

    print(f"Saque de {n}")
    print(f"{nt50} notas de R$50")
    print(f"{nt20} notas de R$20")
    print(f"{nt10} notas de R$10")
    print(f"{nt2} notas de R$2")
    print(f"{nt1} notas de R$1")





