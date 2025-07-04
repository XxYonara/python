vlr = int(input("Qual o valor da sua compra ? "))
soma = int(0)
parc = int(0)
print("Qual a forma de pagamento ?")
print("[1] a vista ou pix.")
print("[2] Cartão de debito")
print("[3] Cartão de credido em até 3 vez")
print("[4] Cartão de credito acima de 3 vezes")
r = int(input(" "))

match r:
    case 1:
        soma = (vlr - (vlr * 0.1) )
        print(f"O valor da compra ficou em {soma}")
    case 2:
        soma = (vlr - (vlr * 0.05))
        print(f"A compra ficou no valor de {soma}")
    case 3:
        p = int(input("Gostaria de parcelar em quantas vezes ?"))
        parc = vlr / p
        soma = ((vlr * 0.05) + vlr)
        print(f"Sua compra de {vlr} parcelada em {p} de {parc} sendo um total de {soma} ")
    case 4:
        p = int(input("Gostaria de parcelar em quantas vezes ?"))
        parc = vlr / p
        soma = ((vlr * 0.1) + vlr)
        print(f"Sua compra de {vlr} parcelada em {p} de {parc} sendo um total de {soma} ")