c = int(0)
soma = int(1)



while (c != 9999):
    c = c + 1
    usu = str(input("Digite seu usuario."))
    senha = str(input("Digite seu usuário."))
    if(usu == "facil" and usu == "ff"):
        print("acesso correto")
    else:
        soma = soma *2
        print(f"A multa é de {soma}")
        r = str(input("Gostaria de de tentar novamente ?"))
        if(r == "não"):
            break

        


