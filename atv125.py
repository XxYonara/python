import atv125fc
n = int(input("Digite um número. "))

t = atv125fc.Dobrar(n)
print(f"O dobro de {n} é {t}")

n2 = int(input("Digite um outro número"))
soma = int(t + n2)
print(f"A soma dos dois números é {soma}")

