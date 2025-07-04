cont = int(0)
somaf = int(0)
for cont in range(0,3,1):
    n = str(input("Digite seu nome."))
    s = str(input("Qual seu sexo ?"))

    if(s == "masculino"):
        somaf = somaf + 1
print(f"Foram cadastrados {somaf} homens")
