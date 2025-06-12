n1 = int(input("Digite um número."))
n2 = int(input("Digite outro número."))
print("[1] soma")
print("[2] subtração")
print("[3] multiplicação")
print("[4] divisão")

s = int(input(""))

match s:
    case 1:
        soma = n1 + n2
        print(str(soma))
    case 2:
        soma = n1 - n2
        print(str(soma))
    case 3:
        soma = n1 * n2
        print(str(soma))
    case 4:
        soma = n1 / n2
        print(str(soma))

