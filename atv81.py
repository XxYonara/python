c = int(0)
soma =int(0)

while (c != 9):
    c = c + 1
    n = int(input("Digite um número."))
    soma = soma + n

    if(n == 999):
        break

print(f"Foram feitas {c} tentativas e a soma dos valores é {soma}.")