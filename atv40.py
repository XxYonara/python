resp = int(input("Qual sua idade?"))

if(resp == 18):
    sexo = str(input("Qual seu sexo?"))
    if(sexo == "masculino"):
      nacionalidade = str(input("Qual a sua nacionalidade?"))
      if(nacionalidade == "brasileiro"):
        print("Bem vindo soldado.")
else:
    print("Dispensado")