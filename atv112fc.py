def Analisar (n1,n2,n3):
    maior = int(0)
    menor = int(999)

    if(n1 > maior):
        maior = n1
    if(n2 > maior):
        maior = n2
    if(n3 > maior):
        maior = n3
    if(n1 < menor):
        menor = n1
    if(n2 < menor):
        menor = n2
    if(n3 < menor):
        menor = n3
    print(f"O maior número é {maior} e o menor é {menor}")