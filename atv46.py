cmp = int(input("Qual o valor da compra ?"))

desc = int(cmp-(cmp * 0.05))

if(cmp > 500):
    print("O valor final da sua compra é "+str(desc))
else:
    print("O valor final da sua compra é "+str(cmp))

