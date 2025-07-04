def Lascado():
    d = int(input("Qual o valor da sua divida ?"))
    t = int(input("Quanto tempo tem essa divida ?"))
    j = float(input("Qual a taxa de juros ?"))

    juros = int (d * t * j)
    total = int(d + juros)

    print(f"O juros de sua divida é de {juros} e total final é {total}")