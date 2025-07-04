c = int(0)
someh = int(0)

for cont in range (0,3,1):
    n = str(input("Digite seu nome. "))
    s = str(input("Qual seu sexo ? "))

    if(s == "h"):
        someh = someh + 1

print(f"Foram cadastrados {someh} homens.")
    