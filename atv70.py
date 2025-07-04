c = int(0)
soma = int(0)


while (c != 2000000):
    c = c + 1
    n = int(input("Digite um número."))
    soma = soma + n
    if(n == 999):
        break

print(f"A soma dos valores é {soma} e a quantidade de tentativas foi {c}.")
