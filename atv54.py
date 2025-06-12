print("Qual humorista voçê escolhe ?")
print("[1] Fabio Porchat")
print("[2] Danilo Gentili")
print("[3] Rafinha Bastos")
r = int(input(""))

match r:
    case 1:
        cid = str(input("Qual a sua cidade?"))
        if(cid == "Araxa"):
            id = str(input("Voçê é maior de idade?"))
            if(id == "sim"):
             print("Tem show do Fabio Porchat")
    case 2:
        cid = str(input("Qual a sua cidade?"))
        if(cid == "São Paulo"):
            print("Tem show do Danilo Gentili")
    case 3:
        cid = str(input("Qual a sua cidade?"))
        if(cid == "Rio grande do sul"):
            print("Tem show do Rafinha Bastos")
    case _:
        print("Não tem show")