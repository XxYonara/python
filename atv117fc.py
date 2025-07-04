def Investigar(a,b,c,d,e):
    cont = int(0)
    if(a == "s"):
        cont = cont + 1
    if(b == "s"):
        cont = cont + 1
    if(c == "s"):
        cont = cont + 1
    if(d == "s"):
        cont = cont + 1
    if(e == "s"):
        cont = cont+ 1
    if(cont == 2):
        print("Suspeita")
    elif(cont >= 3 and cont <= 4):
        print("Cúmplice")
    elif(cont == 5):
        print("Assassino")
    else:
     print("Inocente")