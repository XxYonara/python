n = [0,0,0]
cont = int(0)
cnt = int(0)

for cont in range (3):
    n[cont] =int(input("Digite um número. "))

    if(n[cont] == 14):
        cnt = cnt + 1

print(f"O número 14 apareceu {cnt} vezes")