resp = int(input("Quanto o vendedor vendeu esse mês?"))

if(resp >= 22000):
    ano = int(input("Quantos anos voçê tem na empresa ?"))
    if(ano == 2):
        com1 = float(resp * 0.03)
        print("A comição é "+str(com1))
    if(ano >= 3):
        com2 = float(resp * 0.04)
        print("A comição é "+str(com2))
    if(ano < 2):
        com3 = float(resp * 0.02)
        print("A comição é "+str(com3))
       
