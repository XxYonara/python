c = int(0)
err = int(0)
err2 = int(0)

while (c != 3):
    c = c + 1
    n = str(input("Digite um nome. "))
    id = int(input("Digite sua idade. "))

    if(n == "João" and id > 35):
        break
    elif(n != "João" and id != 35):
        err = err + 1
        print("Bloqueado")
    

    print(f"Foram feitas {err} tentativas de nomes e idades erradas.")


