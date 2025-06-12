n1 = str(input("Solta teia de aranha?"))
n2 = str(input("Quem usa martelo?"))
n3 = str(input("Quem fica verde e muito forte?"))
n4 = str(input("É filho do deus de Asgard?"))
n5 = str(input("Qual heroi tem sua fraqueza como o  calor ?"))
homemaranha= int(0)
thor = int(0)
hulk = int(0)

if(n1 == "sim"):
    homemaranha += 1

if(n2 == "thor"):
    thor += 1

if(n3 == "hulk"):
    hulk += 1

if(n4 == "sim"):
    thor += 1
  
if(n5 == "hulk"):
    hulk += 1


print("Homem aranha tem "+str(homemaranha)+" pontos, e thor tem "+str(thor)+" pontos. Hulk tem "+str(hulk)+" pontos.")