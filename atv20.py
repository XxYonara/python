id = int(input("Qual sua idade?"))
nac = str(input("Qual sua nacionalidade?"))
sex = str(input("Qual seu sexo?"))

if(id >= 18 and nac == str("brasileiro") and sex == str("masculino")):
    print("apto")
else:
    print("não apto")