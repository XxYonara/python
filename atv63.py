c = int(0)
cin = int(0)
tres = int(0)

while (c != 7):
    c = c + 1
    num = int(input("Digite um número."))

    if(num%5==0):
        cin = cin + 1
    if(num%3==0):
        tres = tres +1

print(f"Foram identificados {cin} números que são múltiplos de cinco e {tres} números que são múltiplos por 3")
