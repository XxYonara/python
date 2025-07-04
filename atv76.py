cont = int(0)
total = int(0)

for cont in range (0,10,1):
    num = int(input("Qual tabuada gostaria de ver ?"))

    if(num < 0):
        break

    cont = cont + 1
    total = num * cont
    print(f"{num} x {cont} = {total}")


