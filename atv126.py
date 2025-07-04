import atv126fc
n = [0,0]
cont = int(0)

for cont in range(2):
    
    n[cont] = int(input("Digite um número"))

m = atv126fc.Maior(n[0],n[1])
print(f"O maior número é {m}")

n = atv126fc.Menor(n[0],n[1])
print(f"O menor número é {n}.")

media = float((m + n)/2)
print(f"E a média dos dois é {media}")
