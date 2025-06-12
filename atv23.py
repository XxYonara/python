cmp1 = int(input("Qual o valor da primeira compra ?"))
cmp2 = int(input("Qual o valor da segunda compra ?"))
cmp3 = int(input("Qua o valor da terceira compra ?"))

soma = int(cmp1 + cmp2 + cmp3)
media = int((cmp1 + cmp2 + cmp3)/3)
dobro = int(media * 2)

if(soma > dobro):
    print("verdadeiro")
else:
    print("falso")    