c = int(0)
ab = int(0)
ac = int(0)

while (c != 4):
    c = c + 1
    peso = int(input("Digite seu peso."))
    if(peso <= 70):
        ab = ab + 1
    if(peso > 70):
        ac = ac + 1
print(f"{ac} estão acima do peso médio e existe {ab} pessoas com peso igual ou abaixo da média")
